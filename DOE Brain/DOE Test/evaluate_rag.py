# evaluate_rag_enhanced.py
"""
Enhanced DOE RAG Evaluation Script with Real-Time Metrics
Tracks: Latency, Token Usage, Costs for Production Planning

Updated: Now reads from JSON dataset (previously CSV)
"""

import os
import sys
import json
import pandas as pd
from typing import Dict, List, Tuple
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import time
import traceback
import re
import subprocess
import tiktoken

# Load environment variables
load_dotenv()

# Paths - UPDATED: Now using JSON file
DATASET_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\DOE Test\econometrics_evaluation_dataset.json"
RESULTS_DIR = r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\DOE Test\Results"

# Azure OpenAI Configuration
AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# FAISS Configuration
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings

FAISS_INDEX_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\Normal Rag"
GRAPHRAG_ROOT = r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\Grag"

# ============================================================================
# PRICING CONFIGURATION (Azure OpenAI GPT-4o-mini in INR)
# ============================================================================

PRICING = {
    "gpt-4o-mini": {
        "input": 0.01349719,    # ₹13.49719 per 1M tokens = ₹0.01349719 per 1K tokens
        "output": 0.0539888,    # ₹53.9888 per 1M tokens = ₹0.0539888 per 1K tokens
    }
}

# Ensure results directory exists
os.makedirs(RESULTS_DIR, exist_ok=True)


# ============================================================================
# DATASET LOADING - UPDATED FOR JSON
# ============================================================================

def load_evaluation_dataset(dataset_path: str) -> List[Dict]:
    """
    Load evaluation dataset from JSON file.
    
    Args:
        dataset_path: Path to the JSON file
        
    Returns:
        List of dictionaries containing evaluation questions
    """
    try:
        with open(dataset_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validate required fields
        required_fields = ['question_id', 'question', 'ground_truth_answer', 
                          'question_type', 'complexity', 'retrieval_method', 'topic']
        
        for idx, item in enumerate(data):
            missing_fields = [field for field in required_fields if field not in item]
            if missing_fields:
                print(f"⚠️  Warning: Question at index {idx} missing fields: {missing_fields}")
        
        return data
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset file not found: {dataset_path}")


# ============================================================================
# TOKEN ESTIMATION & COST CALCULATION
# ============================================================================

def estimate_tokens(text: str) -> int:
    """Estimate token count for text."""
    try:
        encoding = tiktoken.encoding_for_model("gpt-4")
        return len(encoding.encode(text))
    except:
        # Fallback: rough estimation (1 token ≈ 4 characters)
        return len(text) // 4


def calculate_cost_inr(input_tokens: int, output_tokens: int, model: str = "gpt-4o-mini") -> float:
    """Calculate cost in INR."""
    pricing = PRICING.get(model, PRICING["gpt-4o-mini"])
    
    input_cost = (input_tokens / 1000) * pricing["input"]
    output_cost = (output_tokens / 1000) * pricing["output"]
    
    return input_cost + output_cost


def sanitize_for_csv(text: str, max_length: int = 32000) -> str:
    """
    Sanitize text for CSV export to avoid parsing issues.
    
    - Replaces newlines with spaces or \\n literal
    - Truncates extremely long content
    - Removes problematic characters
    """
    if not text:
        return ""
    
    # Replace newlines with literal \\n for CSV compatibility
    sanitized = text.replace('\r\n', '\\n').replace('\n', '\\n').replace('\r', '\\n')
    
    # Remove or replace problematic characters
    sanitized = sanitized.replace('\x00', '')  # Null bytes
    
    # Truncate if too long (with indicator)
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + "... [TRUNCATED]"
    
    return sanitized


def create_compact_results(all_results: List[Dict]) -> List[Dict]:
    """
    Create a compact version of results for easier CSV handling.
    Removes large text fields and keeps only metrics.
    """
    compact = []
    for r in all_results:
        compact.append({
            'question_id': r['question_id'],
            'question': r['question'][:200] + '...' if len(r['question']) > 200 else r['question'],
            'question_type': r['question_type'],
            'complexity': r['complexity'],
            'expected_best_method': r['expected_best_method'],
            'topic': r['topic'],
            
            # Local metrics only
            'local_retrieval_latency_sec': r['local_retrieval_latency_sec'],
            'local_generation_latency_sec': r['local_generation_latency_sec'],
            'local_total_latency_sec': r['local_total_latency_sec'],
            'local_total_tokens': r['local_total_tokens'],
            'local_cost_inr': r['local_cost_inr'],
            
            # Global metrics only
            'global_retrieval_latency_sec': r['global_retrieval_latency_sec'],
            'global_generation_latency_sec': r['global_generation_latency_sec'],
            'global_total_latency_sec': r['global_total_latency_sec'],
            'global_total_tokens': r['global_total_tokens'],
            'global_cost_inr': r['global_cost_inr'],
            
            # FAISS metrics only
            'faiss_retrieval_latency_sec': r['faiss_retrieval_latency_sec'],
            'faiss_generation_latency_sec': r['faiss_generation_latency_sec'],
            'faiss_total_latency_sec': r['faiss_total_latency_sec'],
            'faiss_total_tokens': r['faiss_total_tokens'],
            'faiss_cost_inr': r['faiss_cost_inr'],
            
            # Answer lengths (instead of full text)
            'local_answer_length': len(r.get('local_answer', '')),
            'global_answer_length': len(r.get('global_answer', '')),
            'faiss_answer_length': len(r.get('faiss_answer', '')),
            
            'timestamp': r['timestamp']
        })
    return compact


# ============================================================================
# CONTENT CLEANING
# ============================================================================

def clean_graphrag_output(stdout: str, stderr: str) -> Tuple[bool, str]:
    """
    CRITICAL FIX: GraphRAG writes output to STDERR, not STDOUT!
    Check BOTH for content. Also handles traceback/error scenarios.
    
    Returns:
        (is_success, cleaned_content)
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
    VALID_CONTENT_MARKERS = [
        '## ',      # Markdown H2 headers (common in GraphRAG responses)
        '### ',     # Markdown H3 headers
        '# ',       # Markdown H1 headers
        '**',       # Bold text (common in responses)
        '1. ',      # Numbered lists
        '- ',       # Bullet points
    ]
    
    def is_error_line(line: str) -> bool:
        """Check if a line is part of error/debug output."""
        return any(pattern in line for pattern in ERROR_PATTERNS)
    
    def is_valid_content_start(line: str) -> bool:
        """Check if line looks like valid response content."""
        stripped = line.strip()
        if not stripped:
            return False
        # Must start with a content marker or be substantial prose
        for marker in VALID_CONTENT_MARKERS:
            if stripped.startswith(marker):
                return True
        # Check for substantial prose (sentence-like text)
        if len(stripped) > 50 and ' ' in stripped and not is_error_line(stripped):
            # Additional check: should have natural language patterns
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
        
        # Strategy: Find the FIRST valid content line that is NOT preceded by error patterns
        content_start_idx = None
        in_error_block = False
        error_block_depth = 0
        
        for i, line in enumerate(lines):
            # Track if we're in an error/traceback block
            if is_error_line(line):
                in_error_block = True
                error_block_depth = 0
                continue
            
            # After error block, need some clean lines before trusting content
            if in_error_block:
                if line.strip() == '':
                    error_block_depth += 1
                    if error_block_depth >= 2:  # Two blank lines = probably out of error block
                        in_error_block = False
                continue
            
            # Skip known noise patterns
            noise_patterns = ['deprecated', 'INFO:', 'WARN:', 'DEBUG:', 'creating llm',
                             'tiktoken', 'SUCCESS:', 'PS F:', 'PS C:']
            if any(p in line for p in noise_patterns):
                continue
            
            # Check if this looks like valid content
            if is_valid_content_start(line):
                content_start_idx = i
                break
        
        # If we found content start, extract and validate
        if content_start_idx is not None:
            content_lines = []
            for line in lines[content_start_idx:]:
                # Stop if we hit another error block
                if is_error_line(line):
                    break
                content_lines.append(line)
            
            result_text = '\n'.join(content_lines).strip()
            result_text = re.sub(r'\n{3,}', '\n\n', result_text)
            
            # Final validation: should be reasonable size and have actual content
            if len(result_text) > 100 and not is_error_line(result_text[:500]):
                return True, result_text
    
    return False, "⚠️ No content returned from GraphRAG"


# ============================================================================
# RETRIEVAL FUNCTIONS WITH TIMING
# ============================================================================

def retrieve_graphrag_local_improved(query: str) -> Tuple[str, float, int]:
    """
    GraphRAG LOCAL query with timing and token counting.
    
    Returns:
        (context, latency_seconds, context_tokens)
    """
    start_time = time.time()
    
    try:
        cmd = [
            "graphrag",
            "query",
            "--root", GRAPHRAG_ROOT,
            "--method", "local",
            "--query", query
        ]
        
        # Set environment to force UTF-8 encoding
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8:replace'
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=150,
            encoding='utf-8',
            errors='replace',
            env=env
        )
        
        # Check both stderr and stdout for content
        is_success, content = clean_graphrag_output(result.stdout, result.stderr)
        
        latency = time.time() - start_time
        
        if is_success:
            full_content = f"📚 **GraphRAG LOCAL Results**\n\n{content}"
            tokens = estimate_tokens(full_content)
            return full_content, latency, tokens
        else:
            tokens = estimate_tokens(content)
            return content, latency, tokens
        
    except FileNotFoundError:
        latency = time.time() - start_time
        error_msg = "❌ 'graphrag' command not found. Check if graphrag is in PATH."
        return error_msg, latency, 0
    except subprocess.TimeoutExpired:
        latency = 150.0  # Timeout value
        error_msg = "⏱️ Query timed out (150s limit)."
        return error_msg, latency, 0
    except Exception as e:
        latency = time.time() - start_time
        error_msg = f"❌ Error: {type(e).__name__}: {str(e)}"
        return error_msg, latency, 0


def retrieve_graphrag_global_improved(query: str) -> Tuple[str, float, int]:
    """
    GraphRAG GLOBAL query with timing and token counting.
    
    Returns:
        (context, latency_seconds, context_tokens)
    """
    start_time = time.time()
    
    try:
        cmd = [
            "graphrag",
            "query",
            "--root", GRAPHRAG_ROOT,
            "--method", "global",
            "--query", query
        ]
        
        # Set environment to force UTF-8 encoding
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
        
        # Check both stderr and stdout for content
        is_success, content = clean_graphrag_output(result.stdout, result.stderr)
        
        latency = time.time() - start_time
        
        if is_success:
            full_content = f"🌐 **GraphRAG GLOBAL Results**\n\n{content}"
            tokens = estimate_tokens(full_content)
            return full_content, latency, tokens
        else:
            tokens = estimate_tokens(content)
            return content, latency, tokens
        
    except FileNotFoundError:
        latency = time.time() - start_time
        error_msg = "❌ 'graphrag' command not found. Check if graphrag is in PATH."
        return error_msg, latency, 0
    except subprocess.TimeoutExpired:
        latency = 600.0  # Timeout value
        error_msg = "⏱️ Query timed out (600s limit)."
        return error_msg, latency, 0
    except Exception as e:
        latency = time.time() - start_time
        error_msg = f"❌ Error: {type(e).__name__}: {str(e)}"
        return error_msg, latency, 0


def retrieve_faiss_rag_improved(query: str) -> Tuple[str, float, int]:
    """
    FAISS RAG query with timing and token counting.
    
    Returns:
        (context, latency_seconds, context_tokens)
    """
    start_time = time.time()
    
    try:
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        db = FAISS.load_local(
            FAISS_INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = db.similarity_search(query, k=4)
        
        latency = time.time() - start_time
        
        if not docs:
            error_msg = "⚠️ No relevant information found in FAISS index."
            return error_msg, latency, 0
        
        results = ["📚 **DOE Textbook Context (FAISS RAG)**\n"]
        
        for i, doc in enumerate(docs, 1):
            content = doc.page_content.strip()
            results.append(f"\n**Chunk {i}:**\n{content}\n")
        
        full_content = "\n".join(results)
        tokens = estimate_tokens(full_content)
        
        return full_content, latency, tokens
        
    except Exception as e:
        latency = time.time() - start_time
        error_msg = f"❌ Error: {str(e)}"
        return error_msg, latency, 0


# ============================================================================
# ANSWER GENERATION WITH TIMING & TOKEN TRACKING
# ============================================================================

def initialize_llm():
    """Initialize Azure OpenAI LLM."""
    return AzureChatOpenAI(
        azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
        openai_api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        temperature=0.7,
        max_tokens=2000
    )


def generate_answer_from_context(
    llm: AzureChatOpenAI,
    question: str,
    context: str,
    method_name: str
) -> Tuple[str, float, int, int]:
    """
    Generate answer from context with timing and token counting.
    
    Returns:
        (answer, latency_seconds, input_tokens, output_tokens)
    """
    
    # Skip if context retrieval failed
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
        # Estimate input tokens
        input_tokens = estimate_tokens(prompt)
        
        # Generate response
        response = llm.invoke(prompt)
        
        latency = time.time() - start_time
        
        # Get answer and estimate output tokens
        answer = response.content.strip()
        output_tokens = estimate_tokens(answer)
        
        return answer, latency, input_tokens, output_tokens
        
    except Exception as e:
        latency = time.time() - start_time
        error_msg = f"[ERROR: {type(e).__name__}: {str(e)}]"
        return error_msg, latency, 0, 0


# ============================================================================
# MAIN QUERY FUNCTION WITH METRICS
# ============================================================================

def query_all_rag_methods(question: str) -> Dict:
    """
    Query all RAG methods with full metrics tracking.
    
    Returns dict with:
        - contexts, answers
        - retrieval latencies, generation latencies
        - token counts, costs
    """
    
    print("    → Querying GraphRAG Local...")
    local_context, local_retrieval_time, local_context_tokens = retrieve_graphrag_local_improved(question)
    local_status = "✅" if not any(x in local_context for x in ["❌", "⏱️", "⚠️"]) else "❌"
    print(f"      {local_status} Retrieved in {local_retrieval_time:.2f}s ({local_context_tokens} tokens)")
    
    print("    → Querying GraphRAG Global...")
    global_context, global_retrieval_time, global_context_tokens = retrieve_graphrag_global_improved(question)
    global_status = "✅" if not any(x in global_context for x in ["❌", "⏱️", "⚠️"]) else "❌"
    print(f"      {global_status} Retrieved in {global_retrieval_time:.2f}s ({global_context_tokens} tokens)")
    
    print("    → Querying FAISS RAG...")
    faiss_context, faiss_retrieval_time, faiss_context_tokens = retrieve_faiss_rag_improved(question)
    faiss_status = "✅" if not any(x in faiss_context for x in ["❌", "⏱️", "⚠️"]) else "❌"
    print(f"      {faiss_status} Retrieved in {faiss_retrieval_time:.2f}s ({faiss_context_tokens} tokens)")
    
    return {
        'local_context': local_context,
        'local_retrieval_latency': local_retrieval_time,
        'local_context_tokens': local_context_tokens,
        
        'global_context': global_context,
        'global_retrieval_latency': global_retrieval_time,
        'global_context_tokens': global_context_tokens,
        
        'faiss_context': faiss_context,
        'faiss_retrieval_latency': faiss_retrieval_time,
        'faiss_context_tokens': faiss_context_tokens
    }


def generate_all_answers(llm, question: str, contexts: Dict) -> Dict:
    """
    Generate answers from all contexts with full metrics tracking.
    
    Returns dict with:
        - answers
        - generation latencies
        - token counts
        - costs
    """
    
    print("    → Generating answers...")
    
    # Local
    local_answer, local_gen_time, local_in_tokens, local_out_tokens = generate_answer_from_context(
        llm, question, contexts['local_context'], "GraphRAG Local"
    )
    local_gen_cost = calculate_cost_inr(local_in_tokens, local_out_tokens)
    print(f"      Local: {local_gen_time:.2f}s, ₹{local_gen_cost:.4f}")
    
    # Global
    global_answer, global_gen_time, global_in_tokens, global_out_tokens = generate_answer_from_context(
        llm, question, contexts['global_context'], "GraphRAG Global"
    )
    global_gen_cost = calculate_cost_inr(global_in_tokens, global_out_tokens)
    print(f"      Global: {global_gen_time:.2f}s, ₹{global_gen_cost:.4f}")
    
    # FAISS
    faiss_answer, faiss_gen_time, faiss_in_tokens, faiss_out_tokens = generate_answer_from_context(
        llm, question, contexts['faiss_context'], "FAISS RAG"
    )
    faiss_gen_cost = calculate_cost_inr(faiss_in_tokens, faiss_out_tokens)
    print(f"      FAISS: {faiss_gen_time:.2f}s, ₹{faiss_gen_cost:.4f}")
    
    return {
        'local_answer': local_answer,
        'local_generation_latency': local_gen_time,
        'local_input_tokens': local_in_tokens,
        'local_output_tokens': local_out_tokens,
        'local_answer_tokens': local_out_tokens,
        'local_generation_cost': local_gen_cost,
        
        'global_answer': global_answer,
        'global_generation_latency': global_gen_time,
        'global_input_tokens': global_in_tokens,
        'global_output_tokens': global_out_tokens,
        'global_answer_tokens': global_out_tokens,
        'global_generation_cost': global_gen_cost,
        
        'faiss_answer': faiss_answer,
        'faiss_generation_latency': faiss_gen_time,
        'faiss_input_tokens': faiss_in_tokens,
        'faiss_output_tokens': faiss_out_tokens,
        'faiss_answer_tokens': faiss_out_tokens,
        'faiss_generation_cost': faiss_gen_cost
    }


# ============================================================================
# MAIN EVALUATION FUNCTION
# ============================================================================

def evaluate_dataset():
    """
    Main evaluation function with full metrics tracking.
    Now reads from JSON dataset instead of CSV.
    """
    
    print("=" * 80)
    print("ENHANCED DOE RAG EVALUATION - With Real-Time Metrics")
    print("=" * 80)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Dataset: {DATASET_PATH}")
    print(f"Results Directory: {RESULTS_DIR}")
    print("=" * 80)
    print("\n✨ NEW FEATURES:")
    print("  ⏱️  Real-time latency tracking (retrieval + generation)")
    print("  📊 Token counting for all operations")
    print("  💰 Cost calculation in INR")
    print("  📈 Production-ready metrics")
    print("  📄 JSON dataset support (no more formula issues!)")
    print("=" * 80)
    
    # Load dataset - UPDATED: Now using JSON loader
    print("\n📂 Loading evaluation dataset (JSON format)...")
    try:
        dataset = load_evaluation_dataset(DATASET_PATH)
        print(f"✅ Loaded {len(dataset)} questions from JSON")
    except Exception as e:
        print(f"❌ Failed to load dataset: {e}")
        return
    
    # Initialize LLM
    print("\n🤖 Initializing Azure OpenAI LLM...")
    try:
        llm = initialize_llm()
        print("✅ LLM initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize LLM: {e}")
        return
    
    # Prepare results storage
    all_results = []
    
    # Process each question - UPDATED: Now iterating over list of dicts
    print(f"\n🔄 Processing {len(dataset)} questions...")
    print(f"⚠️  GraphRAG Global is SLOW (5-10 min per question)")
    print(f"💡 Total estimated time: {len(dataset) * 8} - {len(dataset) * 12} minutes\n")
    
    for idx, item in enumerate(dataset):
        # Extract fields from JSON item (dict)
        question_id = item['question_id']
        question = item['question']
        ground_truth = item['ground_truth_answer']
        q_type = item['question_type']
        complexity = item['complexity']
        expected_method = item['retrieval_method']
        topic = item['topic']
        
        print(f"[{idx+1}/{len(dataset)}] {question_id}: {question[:60]}...")
        
        # Query all RAG methods (with retrieval metrics)
        context_metrics = query_all_rag_methods(question)
        
        # Generate answers (with generation metrics)
        answer_metrics = generate_all_answers(llm, question, context_metrics)
        
        # Calculate total costs
        local_total_cost = answer_metrics['local_generation_cost']
        global_total_cost = answer_metrics['global_generation_cost']
        faiss_total_cost = answer_metrics['faiss_generation_cost']
        
        # Calculate total latencies
        local_total_latency = context_metrics['local_retrieval_latency'] + answer_metrics['local_generation_latency']
        global_total_latency = context_metrics['global_retrieval_latency'] + answer_metrics['global_generation_latency']
        faiss_total_latency = context_metrics['faiss_retrieval_latency'] + answer_metrics['faiss_generation_latency']
        
        # Store results with all metrics
        result = {
            # Question info
            'question_id': question_id,
            'question': question,
            'ground_truth_answer': ground_truth,
            'question_type': q_type,
            'complexity': complexity,
            'expected_best_method': expected_method,
            'topic': topic,
            
            # GraphRAG Local
            'local_context': context_metrics['local_context'],
            'local_answer': answer_metrics['local_answer'],
            'local_retrieval_latency_sec': context_metrics['local_retrieval_latency'],
            'local_generation_latency_sec': answer_metrics['local_generation_latency'],
            'local_total_latency_sec': local_total_latency,
            'local_context_tokens': context_metrics['local_context_tokens'],
            'local_answer_tokens': answer_metrics['local_answer_tokens'],
            'local_input_tokens': answer_metrics['local_input_tokens'],
            'local_output_tokens': answer_metrics['local_output_tokens'],
            'local_total_tokens': context_metrics['local_context_tokens'] + answer_metrics['local_input_tokens'] + answer_metrics['local_output_tokens'],
            'local_cost_inr': local_total_cost,
            
            # GraphRAG Global
            'global_context': context_metrics['global_context'],
            'global_answer': answer_metrics['global_answer'],
            'global_retrieval_latency_sec': context_metrics['global_retrieval_latency'],
            'global_generation_latency_sec': answer_metrics['global_generation_latency'],
            'global_total_latency_sec': global_total_latency,
            'global_context_tokens': context_metrics['global_context_tokens'],
            'global_answer_tokens': answer_metrics['global_answer_tokens'],
            'global_input_tokens': answer_metrics['global_input_tokens'],
            'global_output_tokens': answer_metrics['global_output_tokens'],
            'global_total_tokens': context_metrics['global_context_tokens'] + answer_metrics['global_input_tokens'] + answer_metrics['global_output_tokens'],
            'global_cost_inr': global_total_cost,
            
            # FAISS RAG
            'faiss_context': context_metrics['faiss_context'],
            'faiss_answer': answer_metrics['faiss_answer'],
            'faiss_retrieval_latency_sec': context_metrics['faiss_retrieval_latency'],
            'faiss_generation_latency_sec': answer_metrics['faiss_generation_latency'],
            'faiss_total_latency_sec': faiss_total_latency,
            'faiss_context_tokens': context_metrics['faiss_context_tokens'],
            'faiss_answer_tokens': answer_metrics['faiss_answer_tokens'],
            'faiss_input_tokens': answer_metrics['faiss_input_tokens'],
            'faiss_output_tokens': answer_metrics['faiss_output_tokens'],
            'faiss_total_tokens': context_metrics['faiss_context_tokens'] + answer_metrics['faiss_input_tokens'] + answer_metrics['faiss_output_tokens'],
            'faiss_cost_inr': faiss_total_cost,
            
            # Timestamp
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        all_results.append(result)
        
        # Show metrics summary
        print(f"\n    📊 Metrics Summary:")
        print(f"       LOCAL:  {local_total_latency:.2f}s, ₹{local_total_cost:.4f}, {result['local_total_tokens']} tokens")
        print(f"       GLOBAL: {global_total_latency:.2f}s, ₹{global_total_cost:.4f}, {result['global_total_tokens']} tokens")
        print(f"       FAISS:  {faiss_total_latency:.2f}s, ₹{faiss_total_cost:.4f}, {result['faiss_total_tokens']} tokens\n")
        
        # Save checkpoint after each question (still as CSV for compatibility)
        checkpoint_df = pd.DataFrame(all_results)
        checkpoint_path = os.path.join(RESULTS_DIR, "checkpoint_enhanced.csv")
        checkpoint_df.to_csv(checkpoint_path, index=False, encoding='utf-8-sig')
        
        # Also save JSON checkpoint for full data integrity
        checkpoint_json_path = os.path.join(RESULTS_DIR, "checkpoint_enhanced.json")
        with open(checkpoint_json_path, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
    
    # Convert to DataFrame for final analysis
    results_df = pd.DataFrame(all_results)
    
    # Save results
    print("\n💾 Saving enhanced results...")
    
    # 1. Full JSON (recommended - no parsing issues)
    combined_json_path = os.path.join(RESULTS_DIR, "combined_all_results_enhanced.json")
    with open(combined_json_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"   ✅ Saved: combined_all_results_enhanced.json (RECOMMENDED - full data)")
    
    # 2. Compact CSV for metrics analysis (no large text fields)
    compact_results = create_compact_results(all_results)
    compact_df = pd.DataFrame(compact_results)
    compact_csv_path = os.path.join(RESULTS_DIR, "metrics_summary.csv")
    compact_df.to_csv(compact_csv_path, index=False, encoding='utf-8-sig')
    print(f"   ✅ Saved: metrics_summary.csv (compact metrics only)")
    
    # 3. Full CSV with sanitized text (for compatibility)
    sanitized_results = []
    for r in all_results:
        sanitized = r.copy()
        # Sanitize all text fields for CSV
        text_fields = ['ground_truth_answer', 'local_context', 'local_answer', 
                      'global_context', 'global_answer', 'faiss_context', 'faiss_answer']
        for field in text_fields:
            if field in sanitized:
                sanitized[field] = sanitize_for_csv(sanitized[field])
        sanitized_results.append(sanitized)
    
    sanitized_df = pd.DataFrame(sanitized_results)
    combined_csv_path = os.path.join(RESULTS_DIR, "combined_all_results_enhanced.csv")
    sanitized_df.to_csv(combined_csv_path, index=False, encoding='utf-8-sig')
    print(f"   ✅ Saved: combined_all_results_enhanced.csv (sanitized for CSV)")
    
    # Summary with costs
    total_cost = (
        results_df['local_cost_inr'].sum() +
        results_df['global_cost_inr'].sum() +
        results_df['faiss_cost_inr'].sum()
    )
    
    avg_latencies = {
        'local': results_df['local_total_latency_sec'].mean(),
        'global': results_df['global_total_latency_sec'].mean(),
        'faiss': results_df['faiss_total_latency_sec'].mean()
    }
    
    # Success statistics
    print("\n" + "=" * 80)
    print("✅ ENHANCED EVALUATION COMPLETED!")
    print("=" * 80)
    
    print(f"\n📊 Performance Metrics:")
    print(f"\n   Average Latencies:")
    print(f"     LOCAL:  {avg_latencies['local']:.2f}s")
    print(f"     GLOBAL: {avg_latencies['global']:.2f}s")
    print(f"     FAISS:  {avg_latencies['faiss']:.2f}s")
    
    print(f"\n   💰 Total Cost: ₹{total_cost:.2f}")
    print(f"     LOCAL:  ₹{results_df['local_cost_inr'].sum():.2f}")
    print(f"     GLOBAL: ₹{results_df['global_cost_inr'].sum():.2f}")
    print(f"     FAISS:  ₹{results_df['faiss_cost_inr'].sum():.2f}")
    
    print(f"\n📂 Results saved to: {RESULTS_DIR}")
    print("=" * 80)


if __name__ == "__main__":
    try:
        evaluate_dataset()
    except KeyboardInterrupt:
        print("\n\n⚠️  Evaluation interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Evaluation failed:")
        print(f"   {type(e).__name__}: {str(e)}")
        traceback.print_exc()