# model_client_wrapper.py
"""
Custom Azure OpenAI Model Client Wrapper - LIST-BASED VERSION
Captures REAL token usage from ALL API calls by appending to a list.
This prevents losing token data when multiple API calls happen in one turn.
"""

from typing import Optional, Sequence, Any
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_core.models import CreateResult, LLMMessage, RequestUsage
import streamlit as st
import time


class TrackedAzureOpenAIChatCompletionClient(AzureOpenAIChatCompletionClient):
    """
    Wrapper around AzureOpenAIChatCompletionClient that tracks token usage.
    Captures real token counts from Azure API and stores them in a LIST.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store cumulative stats
        self._total_prompt_tokens = 0
        self._total_completion_tokens = 0
        self._call_count = 0
    
    async def create(
        self,
        messages: Sequence[LLMMessage],
        **kwargs
    ) -> CreateResult:
        """
        Override create method to capture token usage from Azure API response.
        APPENDS to a list instead of overwriting to capture ALL API calls.
        """
        # Call the parent create method with all parameters
        result = await super().create(messages, **kwargs)
        
        # Capture usage data from the result
        if hasattr(result, 'usage') and result.usage:
            self._call_count += 1
            
            prompt_tokens = result.usage.prompt_tokens
            completion_tokens = result.usage.completion_tokens
            total_tokens = prompt_tokens + completion_tokens
            
            self._total_prompt_tokens += prompt_tokens
            self._total_completion_tokens += completion_tokens
            
            # ✅ CRITICAL FIX: Append to LIST instead of overwriting single value
            if hasattr(st, 'session_state'):
                # Initialize list if not exists
                if 'model_usage_history' not in st.session_state:
                    st.session_state['model_usage_history'] = []
                
                # Append this API call to the list
                usage_entry = {
                    'prompt_tokens': prompt_tokens,
                    'completion_tokens': completion_tokens,
                    'total_tokens': total_tokens,
                    'timestamp': time.time(),
                    'call_number': self._call_count
                }
                
                st.session_state['model_usage_history'].append(usage_entry)
                
                # Also keep the last one for backward compatibility
                st.session_state['last_model_usage'] = usage_entry
            
            print(f"🔵 [Model Client Call #{self._call_count}] Azure API: {prompt_tokens} prompt + {completion_tokens} completion = {total_tokens} total")
            print(f"   Accumulated in history: {len(st.session_state.get('model_usage_history', []))} calls")
        
        return result
    
    def get_total_usage(self) -> dict:
        """Get cumulative usage across all calls"""
        return {
            'total_prompt_tokens': self._total_prompt_tokens,
            'total_completion_tokens': self._total_completion_tokens,
            'total_tokens': self._total_prompt_tokens + self._total_completion_tokens,
            'call_count': self._call_count
        }
    
    def reset_usage(self):
        """Reset usage counters"""
        self._total_prompt_tokens = 0
        self._total_completion_tokens = 0
        self._call_count = 0


def get_pending_usage() -> list:
    """
    Get all pending usage data from session state.
    Returns list of usage dicts.
    """
    if hasattr(st, 'session_state') and 'model_usage_history' in st.session_state:
        return st.session_state['model_usage_history'].copy()
    return []


def pop_usage() -> Optional[dict]:
    """
    Pop the oldest unprocessed usage from the queue (FIFO).
    Returns usage dict or None if queue is empty.
    """
    if hasattr(st, 'session_state') and 'model_usage_history' in st.session_state:
        if len(st.session_state['model_usage_history']) > 0:
            return st.session_state['model_usage_history'].pop(0)
    return None


def clear_usage_history():
    """Clear all pending usage data"""
    if hasattr(st, 'session_state') and 'model_usage_history' in st.session_state:
        count = len(st.session_state['model_usage_history'])
        st.session_state['model_usage_history'] = []
        print(f"🧹 Cleared {count} pending usage entries")


def get_usage_count() -> int:
    """Get count of pending usage entries"""
    if hasattr(st, 'session_state') and 'model_usage_history' in st.session_state:
        return len(st.session_state['model_usage_history'])
    return 0