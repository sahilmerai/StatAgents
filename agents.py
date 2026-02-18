# agents.py - WITH REAL TOKEN TRACKING FROM AZURE API
import asyncio
import os
from typing import Optional, Sequence
import time
from token_tracker import TokenTracker
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.base import Response
from autogen_agentchat.conditions import (
    TextMentionTermination,
    SourceMatchTermination,
    MaxMessageTermination,
)
from autogen_agentchat.messages import BaseAgentEvent, BaseChatMessage
from autogen_agentchat.teams import Swarm
from autogen_agentchat.messages import AgentEvent, ChatMessage, TextMessage, ToolCallRequestEvent, ToolCallExecutionEvent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_core import CancellationToken
from autogen_agentchat.messages import BaseAgentEvent, BaseChatMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from model_client_wrapper import TrackedAzureOpenAIChatCompletionClient, pop_usage, get_usage_count, clear_usage_history
from tool import analyze_csv_data,retrieve_graphrag_local_Doe,retrieve_doe_rag,retrieve_graphrag_local_Eco
from coding.CRY import execute_python_code, execute_python_code_T
from tool import retrieve_Eco_rag,retrieve_statistics_books,retrieve_business_story,retrieve_statistical_test,retrieve_workflow
from reddit1 import reddit_search_all
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.agents import CodeExecutorAgent
from prompts import load_prompt

import streamlit as st
from dotenv import load_dotenv
load_dotenv()

AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")


HOD_PROMPT =  load_prompt("HOD.txt")
EDA_PROMPT =  load_prompt("EDA_agent.txt")
ECONOMETRICS_PROMPT =  load_prompt("econometrc_agent.txt")
REDDIT_PROMPT =  load_prompt("Reddit_agent.txt")
CODE_EXECUTOR_PROMPT =  load_prompt("CodeExecutor_agent.txt")
VISUALIZER_PROMPT =  load_prompt("VISUALIZER_PROMPT.txt")
DPS_PROMPT =  load_prompt("DPS.txt")
TS =  load_prompt("TS.txt")
DOE =  load_prompt("DOE.txt")
ST = load_prompt("statistical_testing_agent.txt")




class TrackableAssistantAgent(AssistantAgent):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Track which agents have had their system prompt loaded this turn
        self._system_prompt_tracked_this_turn = set()
        # Store last known usage for this agent
        self._last_usage = None
    
    async def on_messages_stream(
        self, messages: Sequence[ChatMessage], cancellation_token: CancellationToken
    ):
        # Reset tracking for this turn
        self._system_prompt_tracked_this_turn.clear()
        self._last_usage = None
        
        # Track start time for this agent's turn
        agent_start_time = time.time()
        
        async for msg in super().on_messages_stream(messages, cancellation_token):
            # Track token consumption FIRST
            self._track_tokens(msg, agent_start_time, messages)
            
            # Then track on Streamlit UI
            self._track_response_on_streamlit(msg)
            yield msg

    def _extract_real_tokens(self, msg):
        """
        Extract REAL token counts from Azure OpenAI API response via session state LIST.
        Pops from the queue (FIFO) to get the next unprocessed API call.
        Returns (input_tokens, output_tokens, has_real_tokens)
        """
        input_tokens = 0
        output_tokens = 0
        has_real_tokens = False
        
        # Pop the oldest unprocessed usage from the queue
        usage = pop_usage()
        
        if usage:
            input_tokens = usage.get('prompt_tokens', 0)
            output_tokens = usage.get('completion_tokens', 0)
            has_real_tokens = True
            self._last_usage = usage
            
            remaining = get_usage_count()
            print(f"✅ Real tokens from Azure API (Call #{usage.get('call_number', '?')}): {input_tokens} prompt + {output_tokens} completion = {input_tokens + output_tokens} total")
            print(f"   Remaining in queue: {remaining} API calls")
        else:
            print(f"⚠️ No usage data available in queue - will use estimation")
        
        # If still no tokens and we have stored usage, use it
        if not has_real_tokens and self._last_usage:
            input_tokens = self._last_usage.get('prompt_tokens', 0)
            output_tokens = self._last_usage.get('completion_tokens', 0)
            has_real_tokens = True
            print(f"✅ Using last known usage: {input_tokens} in, {output_tokens} out")
        
        return input_tokens, output_tokens, has_real_tokens

    def _track_tokens(self, msg, start_time, messages):
        """Track token consumption for analytics"""
        tracker = st.session_state.get("token_tracker")
        if not tracker or not tracker.session_id:
            return  # Skip if tracking not active
        
        execution_time = time.time() - start_time
        
        # Handle different message types
        if isinstance(msg, ToolCallRequestEvent):
            # Agent is calling a tool
            for tool in msg.content:
                # Check if this is a transfer/handoff tool
                is_handoff = tool.name.startswith('transfer_to_')
                
                if is_handoff:
                    # Extract target agent from tool name
                    handoff_to = tool.name.replace('transfer_to_', '')
                    # Normalize name (e.g., "eda_agent" -> "EDA_Agent")
                    handoff_to = self._normalize_agent_name(handoff_to)
                    
                    # Estimate tokens for handoff (small amount)
                    input_est = self._estimate_tokens(str(tool.arguments))
                    
                    tracker.track_message(
                        agent_name=msg.source,
                        action_type="handoff",
                        input_tokens=input_est,
                        output_tokens=0,
                        execution_time=execution_time,
                        tool_name=tool.name,
                        handoff_to=handoff_to,
                        content=f"Transferring to {handoff_to}",
                        include_system_prompt=False
                    )
                else:
                    # Regular tool call - estimate tokens
                    tracker.track_message(
                        agent_name=msg.source,
                        action_type="tool_call",
                        input_tokens=self._estimate_tokens(str(tool.arguments)),
                        output_tokens=0,
                        execution_time=execution_time,
                        tool_name=tool.name,
                        content=str(tool.arguments)[:200],
                        include_system_prompt=False
                    )
        
        elif isinstance(msg, TextMessage) and msg.source != "user":
            # Agent is responding with text
            content = msg.content.replace('TERMINATE', '').strip()
            
            # Try to get REAL tokens from API
            input_tokens, output_tokens, has_real_tokens = self._extract_real_tokens(msg)
            
            # If no real tokens, estimate
            if not has_real_tokens:
                input_tokens = self._estimate_tokens(str(messages[-1].content) if messages else "")
                output_tokens = self._estimate_tokens(content)
                print(f"⚠️ Using estimated tokens: {input_tokens} in, {output_tokens} out")
            
            # Track system prompt ONLY if not already tracked this turn
            should_include_prompt = msg.source not in self._system_prompt_tracked_this_turn
            
            if should_include_prompt:
                self._system_prompt_tracked_this_turn.add(msg.source)
                print(f"🔄 Tracking system prompt for {msg.source} (TextMessage)")
            
            # Track response
            tracker.track_message(
                agent_name=msg.source,
                action_type="response",
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                execution_time=execution_time,
                content=content,
                include_system_prompt=should_include_prompt,
                has_real_tokens=has_real_tokens  # NEW: Flag for real vs estimated
            )
        
        elif isinstance(msg, Response):
            # Final response from agent
            if hasattr(msg, 'chat_message') and isinstance(msg.chat_message, TextMessage):
                content = msg.chat_message.content.replace('TERMINATE', '').strip()
                
                # Try to get REAL tokens from API
                input_tokens, output_tokens, has_real_tokens = self._extract_real_tokens(msg)
                
                # If no real tokens, estimate
                if not has_real_tokens:
                    output_tokens = self._estimate_tokens(content)
                    print(f"⚠️ Using estimated tokens for Response: 0 in, {output_tokens} out")
                
                # Track system prompt ONLY if not already tracked this turn
                should_include_prompt = msg.chat_message.source not in self._system_prompt_tracked_this_turn
                
                if should_include_prompt:
                    self._system_prompt_tracked_this_turn.add(msg.chat_message.source)
                    print(f"🔄 Tracking system prompt for {msg.chat_message.source} (Response)")
                
                tracker.track_message(
                    agent_name=msg.chat_message.source,
                    action_type="final_response",
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    execution_time=execution_time,
                    content=content,
                    include_system_prompt=should_include_prompt,
                    has_real_tokens=has_real_tokens  # NEW: Flag for real vs estimated
                )
    
    def _estimate_tokens(self, text: str) -> int:
        """Estimate tokens (1 token ≈ 4 chars) - FALLBACK ONLY"""
        return max(1, len(str(text)) // 4)
    
    def _normalize_agent_name(self, name: str) -> str:
        """Normalize agent name from tool name"""
        # Special cases
        if name == "head_of_the_department":
            return "Head_of_the_Department"
        elif name == "eda_agent":
            return "EDA_Agent"
        elif name == "ts_agent":
            return "TS_Agent"
        elif name == "visualizer_agent":
            return "visualizer_Agent"
        elif name == "data_processing_unit":
            return "Data_processing_unit"
        elif name == "code_executor":
            return "CodeExecutor"
        elif name == "econometric_agent": 
            return "Econometric_Agent"
        elif name == "statistician":
            return "Statistician"
        elif name == "dOE_agent": 
            return "DOE_Agent"
        elif name == "reddit_news_agent" or name == "redditnewsagent":
            return "RedditNewsAgent"
        
        # Default: capitalize each part
        return '_'.join(word.capitalize() for word in name.split('_'))

    def _track_response_on_streamlit(self, msg):
        """Display messages in Streamlit UI"""
        if isinstance(msg, ToolCallRequestEvent):
            content = f"**[{msg.source}] Tool calls requested:**\n- " + "\n- ".join(
                f"`{tool.name}` with arguments `{tool.arguments}`" for tool in msg.content
            )
            st.session_state["messages"].append({"role": "assistant", "content": content})
            with st.chat_message("assistant", avatar="🛠️"):
                st.markdown(content)
        elif isinstance(msg, TextMessage) and msg.source != "user":
            self._handle_text_message(msg)
        elif isinstance(msg, Response) and isinstance(msg.chat_message, TextMessage):
            self._handle_text_message(msg.chat_message)

    def _handle_text_message(self, msg: TextMessage):
        """Handle and display text messages in Streamlit"""
        msg_content = f"**[{msg.source}]**\n{msg.content.replace('TERMINATE', '').strip()}"
        st.session_state["messages"].append({"role": "assistant", "content": msg_content})
        with st.chat_message("assistant"):
            st.markdown(msg_content)


def is_termination_msg(msg):
    return msg.get("content") and "TERMINATE" in msg["content"]


def initialize_agent():
    HOD = TrackedAzureOpenAIChatCompletionClient(
        azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        default_params={
            "temperature": 0.2,
            "top_p": 0.9,
            "frequency_penalty": 0.2,
            "presence_penalty": 0,
            "stop": []
        }
    )

    HOD_Office = TrackableAssistantAgent(
        name="Head_of_the_Department",
        description="Manager agent for market research and data analysis. Delegates to specialists and synthesizes insights",
        model_client=HOD,
        tools=[retrieve_business_story,retrieve_workflow],
        handoffs=["EDA_Agent", "CodeExecutor", "RedditNewsAgent", 
                  "visualizer_Agent", "TS_Agent","DOE_Agent",
                  "Econometric_Agent",
                  "Data_processing_unit","Statistician"],
        reflect_on_tool_use=True,
        system_message=HOD_PROMPT,
    )

    TS_Agent = TrackableAssistantAgent(
        name="TS_Agent",
        description="Time series specialist. Decompose and forecasting and provide visual plots.",
        model_client=HOD,
        tools=[execute_python_code_T],
        reflect_on_tool_use=True,
        system_message=TS,
        handoffs=["Head_of_the_Department"],
    )


    Statistician = TrackableAssistantAgent(
        name="Statistician",
        description="Statistical hypothesis testing specialist - t-tests, ANOVA, chi-square, correlation tests",
        model_client=HOD,
        tools=[retrieve_statistical_test, retrieve_statistics_books, execute_python_code],
        reflect_on_tool_use=True,
        system_message=ST,
        handoffs=["Head_of_the_Department"],
    )


    DOE_Agent = TrackableAssistantAgent(
        name="DOE_Agent",
        description="Design of Experiments specialist. Uses statistical textbooks to explain DOE concepts, factorial designs, and analysis methods",
        model_client=HOD,
        tools=[execute_python_code_T,retrieve_graphrag_local_Doe,retrieve_doe_rag],
        reflect_on_tool_use=True,
        system_message=DOE,
        handoffs=["Head_of_the_Department"],
    )

    Econometric_Agent = TrackableAssistantAgent(
        name="Econometric_Agent",
        description="Econometric modeling and regression specialist",
    model_client=HOD,
    tools=[retrieve_graphrag_local_Eco,retrieve_Eco_rag,execute_python_code],
    reflect_on_tool_use=True,
    system_message=ECONOMETRICS_PROMPT,
    handoffs=["Head_of_the_Department"],
    ) 

    visualizer_Agent = TrackableAssistantAgent(
        name="visualizer_Agent",
        description="visualizer specialist. Analyzes CSD data, Provide the perfect visual with the interpretion",
        model_client=HOD,
        tools=[execute_python_code],
        reflect_on_tool_use=True,
        system_message=VISUALIZER_PROMPT,
        handoffs=["Head_of_the_Department"],
    ) 

    EDA_Agent = TrackableAssistantAgent(
        name="EDA_Agent",
        description="Exploratory Data Analysis specialist. Analyzes CSV data, provides comprehensive statistics, and creates visualizations",
        model_client=HOD,
        tools=[analyze_csv_data],
        reflect_on_tool_use=True,
        system_message=EDA_PROMPT,
        handoffs=["Head_of_the_Department"],
    )    
    
    Data_processing_unit = TrackableAssistantAgent(
        name="Data_processing_unit",
        description="Data Preprocessing specialist. Cleans data, handles missing values and outliers, applies transformations, and saves analysis-ready datasets to Processed_data folder",
        model_client=HOD,
        tools=[analyze_csv_data, execute_python_code],
        reflect_on_tool_use=True,
        system_message=DPS_PROMPT,
        handoffs=["Head_of_the_Department"],
    ) 

    CodeExecutor = TrackableAssistantAgent(
        name="CodeExecutor",
        description="Custom Python code execution. CRITICAL: CSV files MUST use path /data/filename.csv",
        model_client=HOD,
        tools=[execute_python_code],
        reflect_on_tool_use=True,
        system_message=CODE_EXECUTOR_PROMPT,
        handoffs=["Head_of_the_Department"],
    )

    Reddit_model_client = TrackedAzureOpenAIChatCompletionClient(
        azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        default_params={
            "temperature": 0.5,
            "top_p": 0.95,
            "frequency_penalty": 0.3,
            "presence_penalty": 0.2,
            "stop": ["HANDOFF"]
        }
    )

    reddit_agent = TrackableAssistantAgent(
        name="RedditNewsAgent",
        description=(
            "Finds relevant Reddit posts across r/all for a given topic; returns structured results "
            "with titles, links, subreddits, scores, and comment counts."
        ),
        model_client=Reddit_model_client,
        tools=[reddit_search_all],
        reflect_on_tool_use=True,
        system_message=REDDIT_PROMPT,
        handoffs=["Head_of_the_Department"],
    )

    participants = [
        HOD_Office,
        reddit_agent,
        CodeExecutor,
        DOE_Agent,
        visualizer_Agent,
        Data_processing_unit,
        Econometric_Agent,
        TS_Agent,
        EDA_Agent,
        Statistician
    ]

    termination = (
        TextMentionTermination("TERMINATE")
        & SourceMatchTermination("Head_of_the_Department")
    ) | MaxMessageTermination(max_messages=12)

    team = Swarm(
        participants,
        termination_condition=termination,
    )

    return team