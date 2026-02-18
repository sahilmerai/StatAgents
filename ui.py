# ui.py
import os
import asyncio
import inspect
import shutil
from pathlib import Path

import streamlit as st

# ---------------------------
# Sidebar UI
# ---------------------------
def setup_sidebar():
    """
    Sidebar with:
    - Token tracking status
    - 'New Chat' button to reset the conversation and agent
    - Simple CSV upload to ./data/ folder
    """
    with st.sidebar:
        st.header("Chat")

        # --- Token Tracking Status ---
        tracker = st.session_state.get("token_tracker")
        if tracker and tracker.session_id:
            st.success("📊 **Token Tracking Active**")
            
            # Live metrics
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Messages", len(tracker.messages))
            with col2:
                total_cost = sum(msg.cost_inr for msg in tracker.messages)
                # Add system prompt costs
                for load in tracker.system_prompt_loads:
                    total_cost += load.cost_inr
                st.metric("Cost", f"₹{total_cost:.2f}")
            
            # Show system prompt info
            if tracker.system_prompt_loads:
                st.caption(f"System Prompts Loaded: {len(tracker.system_prompt_loads)}")
            
            st.caption(f"Session: {tracker.session_id.split('_')[-2]}")  # Show just timestamp
        else:
            st.info("⏸️ **No Active Session**")
            st.caption("Will start with your first message")
        
        st.divider()

        # --- New Chat ---
        new_chat_clicked = st.button(
            "🗑️ New Chat",
            type="secondary",
            use_container_width=True,
            help="End current session and start fresh"
        )
        if new_chat_clicked:
            _handle_new_chat()

        st.divider()

        # --- CSV Upload ---
        st.subheader("📁 Upload Data")
        
        # Show uploaded files in ./data/
        data_dir = Path("./data/Raw_data")
        if data_dir.exists():
            csv_files = list(data_dir.glob("*.csv"))
            if csv_files:
                st.success(f"📂 **Available CSV files:** ({len(csv_files)})")
                for csv_file in csv_files:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.text(f"📄 {csv_file.name}")
                    with col2:
                        if st.button("🗑️", key=f"del_{csv_file.name}"):
                            csv_file.unlink()
                            st.rerun()
                
                st.divider()
        
        # Upload new CSV
        uploaded = st.file_uploader(
            "Upload a CSV file", 
            type=["csv"], 
            accept_multiple_files=False,
            help="Upload CSV for analysis",
            key="csv_uploader"
        )
        
        if uploaded is not None:
            # Check if already saved (to avoid re-saving on every rerun)
            data_dir = Path("./data/Raw_data")
            data_dir.mkdir(parents=True, exist_ok=True)
            saved_path = data_dir / uploaded.name
            
            # Only save if file doesn't exist
            if not saved_path.exists():
                # Write file
                with open(saved_path, "wb") as f:
                    f.write(uploaded.getbuffer())
                
                st.success(f"✅ **Saved:** `{uploaded.name}`")
                st.info(f"💬 **Now ask in chat:** \n\n\"Analyze {uploaded.name}\"")
            else:
                # File already exists
                st.info(f"📄 File `{uploaded.name}` already uploaded")
                st.caption(f"💬 Ask in chat: \"Analyze {uploaded.name}\"")
        
        st.caption("💡 Upload CSV, then ask agent to analyze it in the chat")


# ---------------------------
# Event handlers / helpers
# ---------------------------
def _run_async_safely(coro):
    """Run an async coroutine safely from a sync context using the app's loop if present."""
    try:
        asyncio.run(coro)
    except RuntimeError:
        try:
            loop = st.session_state.get("event_loop")
            if loop is not None:
                if loop.is_running():
                    loop.create_task(coro)
                else:
                    loop.run_until_complete(coro)
            else:
                # As a last resort, get current loop or run in a new one
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    loop.create_task(coro)
                else:
                    loop.run_until_complete(coro)
        except Exception:
            pass


def _handle_new_chat():
    """Clear chat messages, reset agent, and save token tracking"""
    
    # ✅ END CURRENT TRACKING SESSION
    tracker = st.session_state.get("token_tracker")
    if tracker and tracker.session_id:
        session_name = tracker.session_id
        tracker.end_session(status="completed")
        st.toast(f"📊 Session saved: {session_name}", icon="✅")
        print(f"\n{'='*80}")
        print(f"📊 Token tracking saved for: {session_name}")
        print(f"{'='*80}\n")
    
    # Clear chat history
    st.session_state["messages"] = []

    # Reset agent
    agent = st.session_state.get("agent")
    if agent is not None:
        reset_fn = getattr(agent, "reset", None)
        if callable(reset_fn):
            try:
                result = reset_fn()
                if inspect.isawaitable(result):
                    _run_async_safely(result)
            except Exception:
                pass

    # Remove agent so main.py reinitializes fresh
    st.session_state.pop("agent", None)
    
    st.toast("🧹 Started a new chat", icon="🆕")
    st.rerun()  # Force rerun to show clean state


# ---------------------------
# Chat history renderer
# ---------------------------
def display_chat_history():
    """Display chat history with support for images."""
    for msg in st.session_state["messages"]:
        role = msg["role"]
        content = msg["content"]
        
        # Handle images
        if "image" in msg:
            with st.chat_message(role, avatar="📊" if role == "assistant" else None):
                st.image(msg["image"], caption="Generated Plot")
        else:
            with st.chat_message(role):
                st.markdown(content)