# repair_failed_queries.py
"""
Repair Script for Failed GraphRAG Global Queries
Only re-runs the failed questions and updates the existing results.

This saves time by not re-running all 15 questions.
"""

import os
import sys
import json
import time
import re
import subprocess
from datetime import datetime
from typing import Tuple, List, Dict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# CONFIGURATION - UPDATE THESE PATHS
# ============================================================================

RESULTS_JSON_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\DOE Test\Results\combined_all_results_enhanced.json"
GRAPHRAG_ROOT = r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\Grag"

# Questions that need repair (identified from analysis)
FAILED_QUESTION_IDS = ["DOE_001", "DOE_005"]

# ============================================================================
# IMPROVED CONTENT CLEANING (Same as updated evaluate_rag.py)
# ============================================================================

def clean_graphrag_output(stdout: str, stderr: str) -> Tuple[bool, str]:
    """
    IMPROVED: Better detection of error/debug content vs actual response.
    """
    
    # Patterns that indicate error/debug content (NOT actual response)
    ERROR_PATTERNS = [
        'Traceback', 'locals', 'site-packages', '.py:', 'File "',
        'F:\\Project work', 'F:/Project work', 'WindowsPath(',
        '│', '┌', '└', '├', '┐', '┘', '─',  # Box drawing characters
        'GraphRagConfig(', 'LanguageModelConfig(', 'asyncio.run(',
        'run_global_search', 'run_local_search', '_query_cli',
        'Exception', 'Error:', 'raise ', 'assert '
    ]
    
    # Patterns that indicate valid content
    VALID_CONTENT_MARKERS = ['## ', '### ', '# ', '**', '1. ', '- ']
    
    def is_error_line(line: str) -> bool:
        return any(pattern in line for pattern in ERROR_PATTERNS)
    
    def is_valid_content_start(line: str) -> bool:
        stripped = line.strip()
        if not stripped:
            return False
        for marker in VALID_CONTENT_MARKERS:
            if stripped.startswith(marker):
                return True
        if len(stripped) > 50 and ' ' in stripped and not is_error_line(stripped):
            has_period = '.' in stripped
            has_capital = stripped[0].isupper()
            return has_period or has_capital
        return False
    
    # Try both output sources
    for output_source in [stderr, stdout]:
        if not output_source or len(output_source.strip()) < 10:
            continue
        
        # Clean ANSI codes
        output = re.sub(r'\x1b\[[0-9;]*m', '', output_source)
        lines = output.split('\n')
        
        content_start_idx = None
        in_error_block = False
        error_block_depth = 0
        
        for i, line in enumerate(lines):
            if is_error_line(line):
                in_error_block = True
                error_block_depth = 0
                continue
            
            if in_error_block:
                if line.strip() == '':
                    error_block_depth += 1
                    if error_block_depth >= 2:
                        in_error_block = False
                continue
            
            noise_patterns = ['deprecated', 'INFO:', 'WARN:', 'DEBUG:', 'creating llm',
                             'tiktoken', 'SUCCESS:', 'PS F:', 'PS C:']
            if any(p in line for p in noise_patterns):
                continue
            
            if is_valid_content_start(line):
                content_start_idx = i
                break
        
        if content_start_idx is not None:
            content_lines = []
            for line in lines[content_start_idx:]:
                if is_error_line(line):
                    break
                content_lines.append(line)
            
            result_text = '\n'.join(content_lines).strip()
            result_text = re.sub(r'\n{3,}', '\n\n', result_text)
            
            if len(result_text) > 100 and not is_error_line(result_text[:500]):
                return True, result_text
    
    return False, "⚠️ No content returned from GraphRAG"


# ============================================================================
# GRAPHRAG GLOBAL QUERY
# ============================================================================

def retrieve_graphrag_global(query: str) -> Tuple[str, float, int]:
    """
    GraphRAG GLOBAL query with timing.
    """
    import tiktoken
    
    def estimate_tokens(text: str) -> int:
        try:
            encoding = tiktoken.encoding_for_model("gpt-4")
            return len(encoding.encode(text))
        except:
            return len(text) // 4
    
    start_time = time.time()
    
    try:
        cmd = [
            "graphrag",
            "query",
            "--root", GRAPHRAG_ROOT,
            "--method", "global",
            "--query", query
        ]
        
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8:replace'
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600,
            encoding='utf-8',
            errors='replace',
            env=env
        )
        
        is_success, content = clean_graphrag_output(result.stdout, result.stderr)
        latency = time.time() - start_time
        
        if is_success:
            full_content = f"🌐 **GraphRAG GLOBAL Results**\n\n{content}"
            tokens = estimate_tokens(full_content)
            return full_content, latency, tokens
        else:
            tokens = estimate_tokens(content)
            return content, latency, tokens
        
    except subprocess.TimeoutExpired:
        return "⏱️ Query timed out (600s limit).", 600.0, 0
    except Exception as e:
        latency = time.time() - start_time
        return f"❌ Error: {type(e).__name__}: {str(e)}", latency, 0


# ============================================================================
# ANSWER GENERATION
# ============================================================================

def generate_answer_from_context(question: str, context: str) -> Tuple[str, float, int, int]:
    """
    Generate answer using Azure OpenAI.
    """
    import tiktoken
    from langchain_openai import AzureChatOpenAI
    
    def estimate_tokens(text: str) -> int:
        try:
            encoding = tiktoken.encoding_for_model("gpt-4")
            return len(encoding.encode(text))
        except:
            return len(text) // 4
    
    if any(x in context for x in ["❌", "⏱️", "⚠️"]):
        return "[NO ANSWER - Context retrieval failed]", 0.0, 0, 0
    
    prompt = f"""You are a Design of Experiments (DOE) expert. Answer the question using ONLY the provided context.

**Context:**
{context}

**Question:**
{question}

**Instructions:**
- Use only information from the context above
- If the context doesn't contain enough information, say so
- Be concise but complete
- Use technical DOE terminology when appropriate

**Answer:**"""
    
    start_time = time.time()
    
    try:
        llm = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.7,
            max_tokens=2000
        )
        
        input_tokens = estimate_tokens(prompt)
        response = llm.invoke(prompt)
        latency = time.time() - start_time
        
        answer = response.content.strip()
        output_tokens = estimate_tokens(answer)
        
        return answer, latency, input_tokens, output_tokens
        
    except Exception as e:
        latency = time.time() - start_time
        return f"[ERROR: {type(e).__name__}: {str(e)}]", latency, 0, 0


# ============================================================================
# COST CALCULATION
# ============================================================================

def calculate_cost_inr(input_tokens: int, output_tokens: int) -> float:
    """Calculate cost in INR for GPT-4o-mini."""
    input_cost = (input_tokens / 1000) * 0.01349719
    output_cost = (output_tokens / 1000) * 0.0539888
    return input_cost + output_cost


# ============================================================================
# MAIN REPAIR FUNCTION
# ============================================================================

def repair_failed_queries():
    """
    Main function to repair only failed GraphRAG Global queries.
    """
    
    print("=" * 70)
    print("🔧 REPAIR SCRIPT - Fix Failed GraphRAG Global Queries")
    print("=" * 70)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Results file: {RESULTS_JSON_PATH}")
    print(f"Questions to repair: {FAILED_QUESTION_IDS}")
    print("=" * 70)
    
    # Load existing results
    print("\n📂 Loading existing results...")
    try:
        with open(RESULTS_JSON_PATH, 'r', encoding='utf-8') as f:
            all_results = json.load(f)
        print(f"✅ Loaded {len(all_results)} questions")
    except Exception as e:
        print(f"❌ Failed to load results: {e}")
        return
    
    # Create backup
    backup_path = RESULTS_JSON_PATH.replace('.json', '_backup.json')
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"💾 Backup created: {backup_path}")
    
    # Find and repair failed questions
    repaired_count = 0
    
    for idx, result in enumerate(all_results):
        question_id = result['question_id']
        
        if question_id not in FAILED_QUESTION_IDS:
            continue
        
        question = result['question']
        
        print(f"\n🔄 Repairing {question_id}: {question[:50]}...")
        
        # Re-run GraphRAG Global
        print("   → Querying GraphRAG Global (this may take 5-10 minutes)...")
        global_context, global_retrieval_time, global_context_tokens = retrieve_graphrag_global(question)
        
        # Check if successful
        is_success = not any(x in global_context for x in ["❌", "⏱️", "⚠️"])
        status = "✅" if is_success else "❌"
        print(f"   {status} Retrieved in {global_retrieval_time:.2f}s ({global_context_tokens} tokens)")
        
        if is_success:
            # Generate new answer
            print("   → Generating answer...")
            global_answer, global_gen_time, global_in_tokens, global_out_tokens = generate_answer_from_context(
                question, global_context
            )
            global_gen_cost = calculate_cost_inr(global_in_tokens, global_out_tokens)
            print(f"   ✅ Answer generated in {global_gen_time:.2f}s, ₹{global_gen_cost:.4f}")
            
            # Update the result
            all_results[idx]['global_context'] = global_context
            all_results[idx]['global_answer'] = global_answer
            all_results[idx]['global_retrieval_latency_sec'] = global_retrieval_time
            all_results[idx]['global_generation_latency_sec'] = global_gen_time
            all_results[idx]['global_total_latency_sec'] = global_retrieval_time + global_gen_time
            all_results[idx]['global_context_tokens'] = global_context_tokens
            all_results[idx]['global_answer_tokens'] = global_out_tokens
            all_results[idx]['global_input_tokens'] = global_in_tokens
            all_results[idx]['global_output_tokens'] = global_out_tokens
            all_results[idx]['global_total_tokens'] = global_context_tokens + global_in_tokens + global_out_tokens
            all_results[idx]['global_cost_inr'] = global_gen_cost
            all_results[idx]['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            repaired_count += 1
            print(f"   ✅ {question_id} repaired successfully!")
        else:
            print(f"   ❌ {question_id} still failing - may need manual intervention")
            print(f"      Context preview: {global_context[:200]}...")
    
    # Save updated results
    print("\n💾 Saving repaired results...")
    
    # Save JSON
    with open(RESULTS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"   ✅ Updated: {RESULTS_JSON_PATH}")
    
    # Also save updated CSV
    import pandas as pd
    
    def sanitize_for_csv(text: str, max_length: int = 32000) -> str:
        if not text:
            return ""
        sanitized = text.replace('\r\n', '\\n').replace('\n', '\\n').replace('\r', '\\n')
        sanitized = sanitized.replace('\x00', '')
        if len(sanitized) > max_length:
            sanitized = sanitized[:max_length] + "... [TRUNCATED]"
        return sanitized
    
    sanitized_results = []
    for r in all_results:
        sanitized = r.copy()
        text_fields = ['ground_truth_answer', 'local_context', 'local_answer', 
                      'global_context', 'global_answer', 'faiss_context', 'faiss_answer']
        for field in text_fields:
            if field in sanitized:
                sanitized[field] = sanitize_for_csv(sanitized[field])
        sanitized_results.append(sanitized)
    
    csv_path = RESULTS_JSON_PATH.replace('.json', '.csv')
    pd.DataFrame(sanitized_results).to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"   ✅ Updated: {csv_path}")
    
    # Summary
    print("\n" + "=" * 70)
    print(f"✅ REPAIR COMPLETED!")
    print(f"   Questions repaired: {repaired_count}/{len(FAILED_QUESTION_IDS)}")
    print("=" * 70)


if __name__ == "__main__":
    try:
        repair_failed_queries()
    except KeyboardInterrupt:
        print("\n\n⚠️ Repair interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Repair failed: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()