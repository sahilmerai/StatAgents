# token_tracker.py
"""
Enhanced Token Tracking System for Multi-Agent Analytics
Tracks tokens, costs (INR), execution time, agent performance, tool usage, routing, and system prompts
"""

import os
import json
import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict, field
from collections import defaultdict
import time


# ============================================================================
# PRICING CONFIGURATION (Azure OpenAI GPT-4o-mini in INR)
# ============================================================================

# GPT-4o-mini pricing per 1K tokens in INR
PRICING = {
    "gpt-4o-mini": {
        "input": 0.01349719,    # ₹13.49719 per 1M tokens = ₹0.01349719 per 1K tokens
        "output": 0.0539888,    # ₹53.9888 per 1M tokens = ₹0.0539888 per 1K tokens
    }
}


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class MessageMetrics:
    """Metrics for a single message/interaction"""
    timestamp: str
    step: int
    agent_name: str
    action_type: str
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    system_prompt_tokens: int = 0
    execution_time: float = 0.0
    cost_inr: float = 0.0
    system_prompt_cost_inr: float = 0.0
    tool_name: Optional[str] = None
    handoff_to: Optional[str] = None
    content: str = ""  # FULL CONTENT
    status: str = "success"
    error_message: Optional[str] = None


@dataclass
class SystemPromptLoad:
    """Record of when a system prompt was loaded"""
    timestamp: str
    step: int
    agent_name: str
    tokens: int
    cost_inr: float
    load_number: int


@dataclass
class AgentMetrics:
    """Aggregated metrics for an agent in a session"""
    agent_name: str
    call_count: int = 0
    system_prompt_loads: int = 0
    system_prompt_tokens: int = 0
    conversation_input_tokens: int = 0
    conversation_output_tokens: int = 0
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_tokens: int = 0
    tool_call_tokens: int = 0
    handoff_tokens: int = 0
    total_execution_time: float = 0.0
    system_prompt_cost_inr: float = 0.0
    conversation_cost_inr: float = 0.0
    total_cost_inr: float = 0.0
    tools_used: List[str] = field(default_factory=list)
    handoffs_made: List[str] = field(default_factory=list)
    success_count: int = 0
    error_count: int = 0


@dataclass
class ToolMetrics:
    """Metrics for tool usage"""
    tool_name: str
    agent_name: str
    call_count: int = 0
    total_tokens: int = 0
    total_execution_time: float = 0.0
    total_cost_inr: float = 0.0
    success_count: int = 0
    error_count: int = 0


@dataclass
class HandoffMetrics:
    """Metrics for agent handoffs"""
    from_agent: str
    to_agent: str
    handoff_count: int = 0
    total_tokens: int = 0
    avg_tokens: float = 0.0
    total_cost_inr: float = 0.0


@dataclass
class SessionSummary:
    """Overall session summary"""
    session_id: str
    experiment_id: str
    start_time: str
    end_time: Optional[str] = None
    user_query: str = ""
    user_query_length: int = 0
    user_query_tokens: int = 0
    total_messages: int = 0
    system_prompt_tokens: int = 0
    conversation_input_tokens: int = 0
    conversation_output_tokens: int = 0
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_tokens: int = 0
    total_execution_time: float = 0.0
    system_prompt_cost_inr: float = 0.0
    conversation_cost_inr: float = 0.0
    total_cost_inr: float = 0.0
    agents_involved: List[str] = field(default_factory=list)
    tools_used: List[str] = field(default_factory=list)
    total_handoffs: int = 0
    success_rate: float = 100.0
    status: str = "in_progress"


# ============================================================================
# TOKEN TRACKER CLASS
# ============================================================================

class TokenTracker:
    """Enhanced token tracking system with system prompt tracking"""
    
    def __init__(self, base_dir: str = "./Token"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        
        self.session_id: Optional[str] = None
        self.experiment_dir: Optional[Path] = None
        self.session_start_time: Optional[datetime] = None
        
        self.system_prompts: Dict[str, str] = {}
        self.system_prompt_tokens: Dict[str, int] = {}
        self.system_prompt_loads: List[SystemPromptLoad] = []
        self.agent_prompt_load_count: Dict[str, int] = {}
        
        self.messages: List[MessageMetrics] = []
        self.agent_metrics: Dict[str, AgentMetrics] = {}
        self.tool_metrics: Dict[str, ToolMetrics] = {}
        self.handoff_metrics: Dict[tuple, HandoffMetrics] = {}
        
        self.summary: Optional[SessionSummary] = None
        self.model_name: str = "gpt-4o-mini"
        self.current_step: int = 0
    
    
    def start_session(
        self, 
        user_query: str, 
        model_name: str = "gpt-4o-mini",
        system_prompts: Optional[Dict[str, str]] = None
    ):
        """Start a new tracking session"""
        self.session_start_time = datetime.now()
        timestamp = self.session_start_time.strftime("%Y-%m-%d_%H-%M-%S")
        
        existing_experiments = list(self.base_dir.glob("Experiment_*"))
        experiment_num = len(existing_experiments) + 1
        
        experiment_name = f"Experiment_{experiment_num}_{timestamp}"
        self.experiment_dir = self.base_dir / experiment_name
        self.experiment_dir.mkdir(exist_ok=True)
        
        self.session_id = experiment_name
        self.model_name = model_name
        self.current_step = 0
        
        if system_prompts:
            self.system_prompts = system_prompts
            for agent_name, prompt in system_prompts.items():
                self.system_prompt_tokens[agent_name] = self._estimate_tokens(prompt)
                self.agent_prompt_load_count[agent_name] = 0
        
        self.summary = SessionSummary(
            session_id=self.session_id,
            experiment_id=experiment_name,
            start_time=timestamp,
            user_query=user_query,
            user_query_length=len(user_query),
            user_query_tokens=self._estimate_tokens(user_query)
        )
        
        print(f"📊 Token Tracking Started: {experiment_name}")
        return experiment_name
    
    
    def track_system_prompt_load(self, agent_name: str):
        """Track when a system prompt is loaded"""
        if not self.session_id or agent_name not in self.system_prompt_tokens:
            return
        
        self.current_step += 1
        
        tokens = self.system_prompt_tokens[agent_name]
        cost_inr = self._calculate_cost_inr(tokens, 0)
        
        self.agent_prompt_load_count[agent_name] = self.agent_prompt_load_count.get(agent_name, 0) + 1
        
        load_record = SystemPromptLoad(
            timestamp=datetime.now().isoformat(),
            step=self.current_step,
            agent_name=agent_name,
            tokens=tokens,
            cost_inr=cost_inr,
            load_number=self.agent_prompt_load_count[agent_name]
        )
        
        self.system_prompt_loads.append(load_record)
        
        if agent_name not in self.agent_metrics:
            self.agent_metrics[agent_name] = AgentMetrics(agent_name=agent_name)
        
        am = self.agent_metrics[agent_name]
        am.system_prompt_loads += 1
        am.system_prompt_tokens += tokens
        am.total_input_tokens += tokens
        am.total_tokens += tokens
        am.system_prompt_cost_inr += cost_inr
        am.total_cost_inr += cost_inr
    
    
    def track_message(
        self,
        agent_name: str,
        action_type: str,
        input_tokens: int = 0,
        output_tokens: int = 0,
        execution_time: float = 0.0,
        tool_name: Optional[str] = None,
        handoff_to: Optional[str] = None,
        content: str = "",
        status: str = "success",
        error_message: Optional[str] = None,
        include_system_prompt: bool = False,
        has_real_tokens: bool = False  # NEW: Flag for real vs estimated tokens
    ):
        """Track a single message/interaction"""
        if not self.session_id:
            raise RuntimeError("Session not started. Call start_session() first.")
        
        self.current_step += 1
        
        system_prompt_tokens = 0
        system_prompt_cost = 0.0
        
        if include_system_prompt and agent_name in self.system_prompt_tokens:
            self.track_system_prompt_load(agent_name)
            system_prompt_tokens = self.system_prompt_tokens[agent_name]
            system_prompt_cost = self._calculate_cost_inr(system_prompt_tokens, 0)
        
        total_tokens = input_tokens + output_tokens
        cost_inr = self._calculate_cost_inr(input_tokens, output_tokens)
        
        
        # Log token source (real vs estimated)
        if has_real_tokens:
            print(f"✅ [Step {self.current_step}] {agent_name}: REAL tokens - {input_tokens} in, {output_tokens} out")
        else:
            print(f"⚠️ [Step {self.current_step}] {agent_name}: ESTIMATED tokens - {input_tokens} in, {output_tokens} out")
        msg = MessageMetrics(
            timestamp=datetime.now().isoformat(),
            step=self.current_step,
            agent_name=agent_name,
            action_type=action_type,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            system_prompt_tokens=system_prompt_tokens,
            execution_time=execution_time,
            cost_inr=cost_inr,
            system_prompt_cost_inr=system_prompt_cost,
            tool_name=tool_name,
            handoff_to=handoff_to,
            content=content,
            status=status,
            error_message=error_message
        )
        
        self.messages.append(msg)
        self._update_agent_metrics(agent_name, msg)
        
        if tool_name:
            self._update_tool_metrics(tool_name, agent_name, msg)
        
        if handoff_to:
            self._update_handoff_metrics(agent_name, handoff_to, msg)
        
        return msg
    
    
    def end_session(self, status: str = "completed"):
        """End tracking session and save all data"""
        if not self.session_id:
            print("⚠️ No active session to end")
            return
        
        self.summary.end_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.summary.total_messages = len(self.messages)
        self.summary.status = status
        
        for msg in self.messages:
            self.summary.conversation_input_tokens += msg.input_tokens
            self.summary.conversation_output_tokens += msg.output_tokens
            self.summary.total_input_tokens += msg.input_tokens
            self.summary.total_output_tokens += msg.output_tokens
            self.summary.total_tokens += msg.total_tokens
            self.summary.total_execution_time += msg.execution_time
            self.summary.conversation_cost_inr += msg.cost_inr
            self.summary.total_cost_inr += msg.cost_inr
        
        for load in self.system_prompt_loads:
            self.summary.system_prompt_tokens += load.tokens
            self.summary.system_prompt_cost_inr += load.cost_inr
            self.summary.total_input_tokens += load.tokens
            self.summary.total_tokens += load.tokens
            self.summary.total_cost_inr += load.cost_inr
        
        self.summary.agents_involved = list(self.agent_metrics.keys())
        self.summary.tools_used = list(set(
            msg.tool_name for msg in self.messages if msg.tool_name
        ))
        self.summary.total_handoffs = sum(
            hm.handoff_count for hm in self.handoff_metrics.values()
        )
        
        success = sum(1 for msg in self.messages if msg.status == "success")
        self.summary.success_rate = (success / len(self.messages) * 100) if self.messages else 100.0
        
        self._save_all_data()
        
        print(f"✅ Session Ended: {self.session_id}")
        print(f"   Total Tokens: {self.summary.total_tokens:,}")
        print(f"     - System Prompts: {self.summary.system_prompt_tokens:,}")
        print(f"     - Conversation: {self.summary.conversation_input_tokens + self.summary.conversation_output_tokens:,}")
        print(f"   Total Cost: ₹{self.summary.total_cost_inr:.2f}")
        print(f"     - System Prompts: ₹{self.summary.system_prompt_cost_inr:.2f}")
        print(f"     - Conversation: ₹{self.summary.conversation_cost_inr:.2f}")
        print(f"   Duration: {self.summary.total_execution_time:.2f}s")
        
        self._reset()
    
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation"""
        return len(text) // 4
    
    
    def _calculate_cost_inr(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost in INR"""
        pricing = PRICING.get(self.model_name, PRICING["gpt-4o-mini"])
        input_cost = (input_tokens / 1000) * pricing["input"]
        output_cost = (output_tokens / 1000) * pricing["output"]
        return input_cost + output_cost
    
    
    def _update_agent_metrics(self, agent_name: str, msg: MessageMetrics):
        """Update aggregated agent metrics"""
        if agent_name not in self.agent_metrics:
            self.agent_metrics[agent_name] = AgentMetrics(agent_name=agent_name)
        
        am = self.agent_metrics[agent_name]
        am.call_count += 1
        am.conversation_input_tokens += msg.input_tokens
        am.conversation_output_tokens += msg.output_tokens
        am.total_input_tokens += msg.input_tokens
        am.total_output_tokens += msg.output_tokens
        am.total_tokens += msg.total_tokens
        am.total_execution_time += msg.execution_time
        am.conversation_cost_inr += msg.cost_inr
        am.total_cost_inr += msg.cost_inr
        
        if msg.tool_name and msg.tool_name not in am.tools_used:
            am.tools_used.append(msg.tool_name)
            am.tool_call_tokens += msg.total_tokens
        
        if msg.handoff_to and msg.handoff_to not in am.handoffs_made:
            am.handoffs_made.append(msg.handoff_to)
            am.handoff_tokens += msg.total_tokens
        
        if msg.status == "success":
            am.success_count += 1
        else:
            am.error_count += 1
    
    
    def _update_tool_metrics(self, tool_name: str, agent_name: str, msg: MessageMetrics):
        """Update tool usage metrics"""
        key = f"{agent_name}_{tool_name}"
        
        if key not in self.tool_metrics:
            self.tool_metrics[key] = ToolMetrics(tool_name=tool_name, agent_name=agent_name)
        
        tm = self.tool_metrics[key]
        tm.call_count += 1
        tm.total_tokens += msg.total_tokens
        tm.total_execution_time += msg.execution_time
        tm.total_cost_inr += msg.cost_inr
        
        if msg.status == "success":
            tm.success_count += 1
        else:
            tm.error_count += 1
    
    
    def _update_handoff_metrics(self, from_agent: str, to_agent: str, msg: MessageMetrics):
        """Update handoff metrics"""
        key = (from_agent, to_agent)
        
        if key not in self.handoff_metrics:
            self.handoff_metrics[key] = HandoffMetrics(from_agent=from_agent, to_agent=to_agent)
        
        hm = self.handoff_metrics[key]
        hm.handoff_count += 1
        hm.total_tokens += msg.total_tokens
        hm.total_cost_inr += msg.cost_inr
        hm.avg_tokens = hm.total_tokens / hm.handoff_count
    
    
    def _save_all_data(self):
        """Save all tracking data to files"""
        if not self.experiment_dir:
            return
        
        print("\n📦 Saving tracking data...")
        
        self._save_session_summary()
        self._save_agent_performance()
        self._save_tool_analytics()
        self._save_routing_data()
        self._save_system_prompts_tracking()
        self._save_system_prompts_summary()
        self._save_system_prompts_full()
        self._save_detailed_log()
        self._save_conversation_flow()
    
    
    def _save_session_summary(self):
        """Save session summary"""
        file_path = self.experiment_dir / "session_summary.csv"
        
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'session_id', 'experiment_id', 'start_time', 'end_time',
                'user_query', 'user_query_length', 'user_query_tokens',
                'total_messages', 
                'system_prompt_tokens', 'conversation_input_tokens', 'conversation_output_tokens',
                'total_input_tokens', 'total_output_tokens', 'total_tokens',
                'total_execution_time',
                'system_prompt_cost_inr', 'conversation_cost_inr', 'total_cost_inr',
                'agents_involved', 'tools_used', 'total_handoffs', 
                'success_rate', 'status'
            ])
            writer.writeheader()
            
            row = asdict(self.summary)
            row['agents_involved'] = ', '.join(row['agents_involved'])
            row['tools_used'] = ', '.join(row['tools_used'])
            writer.writerow(row)
        
        print(f"   💾 Saved: session_summary.csv")
    
    
    def _save_agent_performance(self):
        """Save agent performance"""
        file_path = self.experiment_dir / "agent_performance.csv"
        
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'agent_name', 'call_count', 
                'system_prompt_loads', 'system_prompt_tokens',
                'conversation_input_tokens', 'conversation_output_tokens',
                'total_input_tokens', 'total_output_tokens', 'total_tokens',
                'tool_call_tokens', 'handoff_tokens', 'total_execution_time',
                'system_prompt_cost_inr', 'conversation_cost_inr', 'total_cost_inr',
                'tools_used', 'handoffs_made',
                'success_count', 'error_count', 'success_rate'
            ])
            writer.writeheader()
            
            for metrics in self.agent_metrics.values():
                row = asdict(metrics)
                row['tools_used'] = ', '.join(row['tools_used'])
                row['handoffs_made'] = ', '.join(row['handoffs_made'])
                row['success_rate'] = (
                    metrics.success_count / metrics.call_count * 100
                    if metrics.call_count > 0 else 100.0
                )
                writer.writerow(row)
        
        print(f"   💾 Saved: agent_performance.csv")
    
    
    def _save_tool_analytics(self):
        """Save tool analytics"""
        file_path = self.experiment_dir / "tool_analytics.csv"
        
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'tool_name', 'agent_name', 'call_count', 'total_tokens',
                'total_execution_time', 'total_cost_inr', 'success_count',
                'error_count', 'success_rate', 'avg_tokens_per_call',
                'avg_time_per_call'
            ])
            writer.writeheader()
            
            for metrics in self.tool_metrics.values():
                row = asdict(metrics)
                row['success_rate'] = (
                    metrics.success_count / metrics.call_count * 100
                    if metrics.call_count > 0 else 100.0
                )
                row['avg_tokens_per_call'] = (
                    metrics.total_tokens / metrics.call_count
                    if metrics.call_count > 0 else 0
                )
                row['avg_time_per_call'] = (
                    metrics.total_execution_time / metrics.call_count
                    if metrics.call_count > 0 else 0
                )
                writer.writerow(row)
        
        print(f"   💾 Saved: tool_analytics.csv")
    
    
    def _save_routing_data(self):
        """Save routing data"""
        json_path = self.experiment_dir / "routing_data.json"
        routing_data = {
            'handoffs': [asdict(hm) for hm in self.handoff_metrics.values()],
            'routing_summary': {
                'total_handoffs': sum(hm.handoff_count for hm in self.handoff_metrics.values()),
                'unique_routes': len(self.handoff_metrics),
                'most_common_handoff': self._get_most_common_handoff()
            }
        }
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(routing_data, f, indent=2)
        
        csv_path = self.experiment_dir / "routing_data.csv"
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'from_agent', 'to_agent', 'handoff_count', 'total_tokens',
                'avg_tokens', 'total_cost_inr'
            ])
            writer.writeheader()
            writer.writerows([asdict(hm) for hm in self.handoff_metrics.values()])
        
        print(f"   💾 Saved: routing_data.json, routing_data.csv")
    
    
    def _save_system_prompts_tracking(self):
        """Save system prompt loads"""
        file_path = self.experiment_dir / "system_prompts_tracking.csv"
        
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'step', 'timestamp', 'agent_name', 'tokens', 'cost_inr', 'load_number'
            ])
            writer.writeheader()
            
            for load in self.system_prompt_loads:
                writer.writerow(asdict(load))
        
        print(f"   💾 Saved: system_prompts_tracking.csv")
    
    
    def _save_system_prompts_summary(self):
        """Save system prompts summary"""
        file_path = self.experiment_dir / "system_prompts_summary.csv"
        
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'agent_name', 'prompt_tokens', 'times_loaded', 'total_tokens', 'total_cost_inr'
            ])
            writer.writeheader()
            
            summary_data = {}
            for load in self.system_prompt_loads:
                if load.agent_name not in summary_data:
                    summary_data[load.agent_name] = {
                        'agent_name': load.agent_name,
                        'prompt_tokens': load.tokens,
                        'times_loaded': 0,
                        'total_tokens': 0,
                        'total_cost_inr': 0.0
                    }
                summary_data[load.agent_name]['times_loaded'] += 1
                summary_data[load.agent_name]['total_tokens'] += load.tokens
                summary_data[load.agent_name]['total_cost_inr'] += load.cost_inr
            
            for data in summary_data.values():
                writer.writerow(data)
        
        print(f"   💾 Saved: system_prompts_summary.csv")
    
    
    def _save_system_prompts_full(self):
        """Save full system prompts"""
        file_path = self.experiment_dir / "system_prompts_full.txt"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("COMPLETE SYSTEM PROMPTS - REFERENCE\n")
            f.write(f"Session: {self.session_id}\n")
            f.write("="*80 + "\n\n")
            
            for agent_name, prompt_text in self.system_prompts.items():
                tokens = self.system_prompt_tokens.get(agent_name, 0)
                
                f.write(f"[Agent: {agent_name}]\n")
                f.write(f"Tokens: {tokens}\n")
                f.write("-"*80 + "\n")
                f.write(prompt_text)
                f.write("\n" + "-"*80 + "\n\n")
        
        print(f"   💾 Saved: system_prompts_full.txt")
    
    
    def _save_detailed_log(self):
        """Save detailed JSON log"""
        file_path = self.experiment_dir / "detailed_log.json"
        
        log_data = {
            'session_summary': asdict(self.summary),
            'system_prompt_loads': [asdict(load) for load in self.system_prompt_loads],
            'messages': [asdict(msg) for msg in self.messages],
            'agent_metrics': {k: asdict(v) for k, v in self.agent_metrics.items()},
            'tool_metrics': {k: asdict(v) for k, v in self.tool_metrics.items()},
            'handoff_metrics': {f"{k[0]}->{k[1]}": asdict(v) for k, v in self.handoff_metrics.items()}
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"   💾 Saved: detailed_log.json")
    
    
    def _save_conversation_flow(self):
        """Save conversation flow with full content"""
        file_path = self.experiment_dir / "conversation_flow.txt"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write(f"CONVERSATION FLOW - {self.session_id}\n")
            f.write("="*80 + "\n\n")
            
            f.write(f"User Query: {self.summary.user_query}\n")
            f.write(f"Start Time: {self.summary.start_time}\n")
            f.write(f"End Time: {self.summary.end_time}\n")
            f.write(f"Total Duration: {self.summary.total_execution_time:.2f}s\n\n")
            
            f.write(f"COST BREAKDOWN:\n")
            f.write(f"  System Prompts: ₹{self.summary.system_prompt_cost_inr:.2f} ({self.summary.system_prompt_tokens:,} tokens)\n")
            f.write(f"  Conversation: ₹{self.summary.conversation_cost_inr:.2f} ({self.summary.conversation_input_tokens + self.summary.conversation_output_tokens:,} tokens)\n")
            f.write(f"  Total Cost: ₹{self.summary.total_cost_inr:.2f} ({self.summary.total_tokens:,} tokens)\n\n")
            
            f.write("-"*80 + "\n")
            f.write("COMPLETE MESSAGE FLOW\n")
            f.write("-"*80 + "\n\n")
            
            for msg in self.messages:
                f.write(f"Step {msg.step}: [{msg.agent_name}] {msg.action_type}\n")
                f.write(f"  Time: {msg.timestamp}\n")
                
                if msg.system_prompt_tokens > 0:
                    f.write(f"  Tokens: {msg.input_tokens} in + {msg.output_tokens} out = {msg.total_tokens} total\n")
                    f.write(f"          (includes system prompt: {msg.system_prompt_tokens} tokens)\n")
                else:
                    f.write(f"  Tokens: {msg.input_tokens} in + {msg.output_tokens} out = {msg.total_tokens} total\n")
                
                f.write(f"  Duration: {msg.execution_time:.2f}s\n")
                
                if msg.system_prompt_cost_inr > 0:
                    f.write(f"  Cost: ₹{msg.cost_inr + msg.system_prompt_cost_inr:.4f} (conversation: ₹{msg.cost_inr:.4f} + system prompt: ₹{msg.system_prompt_cost_inr:.4f})\n")
                else:
                    f.write(f"  Cost: ₹{msg.cost_inr:.4f}\n")
                
                if msg.tool_name:
                    f.write(f"  Tool: {msg.tool_name}\n")
                if msg.handoff_to:
                    f.write(f"  Handoff to: {msg.handoff_to}\n")
                
                if msg.content:
                    f.write(f"\n  Full Content:\n")
                    for line in msg.content.split('\n'):
                        f.write(f"  {line}\n")
                    f.write("\n")
                
                if msg.status != "success":
                    f.write(f"  Status: {msg.status}\n")
                    if msg.error_message:
                        f.write(f"  Error: {msg.error_message}\n")
                
                f.write("\n")
            
            f.write("="*80 + "\n")
        
        print(f"   💾 Saved: conversation_flow.txt")
    
    
    def _get_most_common_handoff(self) -> Optional[str]:
        """Get most common handoff"""
        if not self.handoff_metrics:
            return None
        
        max_handoff = max(self.handoff_metrics.values(), key=lambda x: x.handoff_count)
        return f"{max_handoff.from_agent} -> {max_handoff.to_agent} ({max_handoff.handoff_count} times)"
    
    
    def _reset(self):
        """Reset tracker"""
        self.session_id = None
        self.experiment_dir = None
        self.session_start_time = None
        self.system_prompts = {}
        self.system_prompt_tokens = {}
        self.system_prompt_loads = []
        self.agent_prompt_load_count = {}
        self.messages = []
        self.agent_metrics = {}
        self.tool_metrics = {}
        self.handoff_metrics = {}
        self.summary = None
        self.current_step = 0


def create_tracker(base_dir: str = "./Token") -> TokenTracker:
    """Create and return a new TokenTracker instance"""
    return TokenTracker(base_dir=base_dir)