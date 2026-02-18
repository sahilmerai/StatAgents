# main.py
import streamlit as st
import sys
import asyncio
import os
from PIL import Image
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage
from token_tracker import create_tracker
from agents import initialize_agent
from ui import setup_sidebar, display_chat_history
from prompts import load_prompt

st.header("StatAgents")

# Windows compatibility
if sys.platform == "win32":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    except Exception:
        pass

# App-wide event loop
if "event_loop" not in st.session_state:
    st.session_state["event_loop"] = asyncio.new_event_loop()
    asyncio.set_event_loop(st.session_state["event_loop"])

# Chat messages state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Initialize token tracker (ONCE)
if "token_tracker" not in st.session_state:
    st.session_state["token_tracker"] = create_tracker(base_dir="./Token")

# Initialize agent
if "agent" not in st.session_state:
    st.session_state["agent"] = initialize_agent()

# Sidebar
setup_sidebar()

# Show existing chat history
display_chat_history()

# User input
user_query = st.chat_input("How can I help you with your marketing strategy?")
if user_query:
    if user_query.strip() == "":
        st.warning("Please enter a query.")
    else:
        tracker = st.session_state["token_tracker"]
        
        # ✅ START SESSION ONLY IF NOT ALREADY ACTIVE
        if not tracker.session_id:
            # Load all system prompts
            system_prompts = {
                "Head_of_the_Department": load_prompt("HOD.txt"),
                "EDA_Agent": load_prompt("EDA_agent.txt"),
                "TS_Agent": load_prompt("TS.txt"),
                "visualizer_Agent": load_prompt("VISUALIZER_PROMPT.txt"),
                "Data_processing_unit": load_prompt("DPS.txt"),
                "CodeExecutor": load_prompt("CodeExecutor_agent.txt"),
                "RedditNewsAgent": load_prompt("Reddit_agent.txt"),
                "Econometric_Agent": load_prompt("econometrc_agent.txt"),
                "DOE_Agent": load_prompt("DOE.txt"),

            }
            
            experiment_id = tracker.start_session(
                user_query=user_query,
                model_name="gpt-4o-mini",  # Azure OpenAI GPT-4o-mini
                system_prompts=system_prompts  # Pass all system prompts
            )
            st.toast(f"📊 Session started: {experiment_id}", icon="📊")
        
        # Track user's message
        tracker.track_message(
            agent_name="User",
            action_type="query",
            output_tokens=len(user_query) // 4,
            content=user_query  # FULL CONTENT
        )
        
        # Add user message to history
        st.session_state["messages"].append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # Track existing images before execution
        output_dir = "./data/Output/Plots"
        existing_images = set()
        if os.path.exists(output_dir):
            existing_images = set(f for f in os.listdir(output_dir) if f.endswith('.png'))

        async def initiate_chat():
            # Run the agent
            await st.session_state["agent"].run(
                task=[TextMessage(content=user_query, source="user")],
                cancellation_token=CancellationToken(),
            )

        # Execute agent
        try:
            st.session_state["event_loop"].run_until_complete(initiate_chat())
            
            # Check for NEW images after agent completes
            if os.path.exists(output_dir):
                current_images = set(f for f in os.listdir(output_dir) if f.endswith('.png'))
                new_images = current_images - existing_images
                
                if new_images:
                    # Display all new images
                    for img_name in sorted(new_images):
                        img_path = os.path.join(output_dir, img_name)
                        with st.chat_message("assistant", avatar="📊"):
                            st.image(img_path, caption=f"Generated Plot: {img_name}")
                            # Also add to message history
                            st.session_state["messages"].append({
                                "role": "assistant", 
                                "content": f"![Plot]({img_path})",
                                "image": img_path
                            })
                        
        except Exception as e:
            st.error(f"Agent error: {e}")
            
            # End session on error
            tracker = st.session_state.get("token_tracker")
            if tracker and tracker.session_id:
                tracker.end_session(status="error")