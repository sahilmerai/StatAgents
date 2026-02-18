# calculate_metrics_v3.py
"""
Calculate RAG Evaluation Metrics - Version 3
Works with Enhanced Evaluation Data (Real Latency, Tokens, Costs)
Adds: Quality Metrics (7), Conciseness, Uncertainty Detection
"""

import os
import pandas as pd
from typing import Dict, List, Tuple
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time
import re

# Load environment
load_dotenv()

# Paths - NOW USES ENHANCED RESULTS
RESULTS_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\ECO Brain\Test\Results\combined_all_results_enhanced.csv"
METRICS_OUTPUT = r"F:\Project work\Cafe Restaurant Analysis\Agents\ECO Brain\Test\Results\metrics_summary.csv"

# Azure OpenAI Configuration
AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")


def initialize_llm():
    """Initialize Azure OpenAI for LLM-as-judge."""
    return AzureChatOpenAI(
        azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
        openai_api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        temperature=0.0,
        max_tokens=500
    )


def initialize_embeddings():
    """Initialize Azure OpenAI embeddings."""
    return AzureOpenAIEmbeddings(
        azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY")
    )


# ============================================================================
# QUALITY METRICS (Original 5 + Conciseness + Uncertainty)
# ============================================================================

def calculate_faithfulness(llm: AzureChatOpenAI, context: str, answer: str) -> float:
    """Calculate faithfulness score."""
    if not answer or len(answer.strip()) < 10 or "[NO ANSWER]" in answer or "[ERROR]" in answer:
        return 0.0
    
    prompt = f"""You are evaluating if an answer is faithful to the provided context.

**Context:**
{context}

**Answer:**
{answer}

**Task:**
Rate faithfulness from 0 to 1:
- 1.0 = All statements in the answer are supported by the context
- 0.5 = Some statements are supported, some are not
- 0.0 = Answer contradicts context or adds unsupported information

Respond with ONLY a number between 0 and 1 (e.g., 0.8)

**Faithfulness Score:**"""

    try:
        response = llm.invoke(prompt)
        score = float(response.content.strip())
        return max(0.0, min(1.0, score))
    except:
        return 0.5


def calculate_answer_relevance(llm: AzureChatOpenAI, question: str, answer: str) -> float:
    """Calculate answer relevance score."""
    if not answer or len(answer.strip()) < 10 or "[NO ANSWER]" in answer or "[ERROR]" in answer:
        return 0.0
    
    prompt = f"""You are evaluating if an answer is relevant to the question asked.

**Question:**
{question}

**Answer:**
{answer}

**Task:**
Rate relevance from 0 to 1:
- 1.0 = Answer directly addresses the question completely
- 0.5 = Answer is somewhat related but incomplete or off-topic
- 0.0 = Answer doesn't address the question at all

Respond with ONLY a number between 0 and 1 (e.g., 0.9)

**Relevance Score:**"""

    try:
        response = llm.invoke(prompt)
        score = float(response.content.strip())
        return max(0.0, min(1.0, score))
    except:
        return 0.5


def calculate_context_precision(llm: AzureChatOpenAI, question: str, context: str) -> float:
    """Calculate context precision score."""
    if not context or len(context.strip()) < 10 or "❌" in context or "⚠️" in context:
        return 0.0
    
    prompt = f"""You are evaluating if retrieved context is relevant to answering a question.

**Question:**
{question}

**Retrieved Context:**
{context}

**Task:**
Rate how much of the retrieved context is actually relevant to answering the question:
- 1.0 = All retrieved information is relevant
- 0.5 = About half is relevant
- 0.0 = None of the retrieved information is relevant

Respond with ONLY a number between 0 and 1 (e.g., 0.7)

**Context Precision Score:**"""

    try:
        response = llm.invoke(prompt)
        score = float(response.content.strip())
        return max(0.0, min(1.0, score))
    except:
        return 0.5


def calculate_context_recall(llm: AzureChatOpenAI, ground_truth: str, context: str) -> float:
    """Calculate context recall score."""
    if not context or len(context.strip()) < 10 or "❌" in context or "⚠️" in context:
        return 0.0
    
    prompt = f"""You are evaluating if retrieved context contains all information from ground truth.

**Ground Truth Answer:**
{ground_truth}

**Retrieved Context:**
{context}

**Task:**
Rate how much of the ground truth information is present in the retrieved context:
- 1.0 = All ground truth information is present in context
- 0.5 = About half of ground truth information is present
- 0.0 = None of ground truth information is present

Respond with ONLY a number between 0 and 1 (e.g., 0.85)

**Context Recall Score:**"""

    try:
        response = llm.invoke(prompt)
        score = float(response.content.strip())
        return max(0.0, min(1.0, score))
    except:
        return 0.5


def calculate_correctness(embeddings, llm: AzureChatOpenAI, ground_truth: str, answer: str) -> float:
    """Calculate correctness score (semantic + LLM)."""
    if not answer or len(answer.strip()) < 10 or "[NO ANSWER]" in answer or "[ERROR]" in answer:
        return 0.0
    
    # Semantic similarity
    try:
        gt_embedding = embeddings.embed_query(ground_truth)
        ans_embedding = embeddings.embed_query(answer)
        semantic_score = cosine_similarity([gt_embedding], [ans_embedding])[0][0]
        semantic_score = max(0.0, min(1.0, semantic_score))
    except:
        semantic_score = 0.5
    
    # LLM judgment
    prompt = f"""You are evaluating if an answer is correct compared to ground truth.

**Ground Truth:**
{ground_truth}

**Generated Answer:**
{answer}

**Task:**
Rate correctness from 0 to 1:
- 1.0 = Answer is factually correct and complete
- 0.5 = Answer is partially correct
- 0.0 = Answer is incorrect or contradicts ground truth

Respond with ONLY a number between 0 and 1 (e.g., 0.95)

**Correctness Score:**"""

    try:
        response = llm.invoke(prompt)
        llm_score = float(response.content.strip())
        llm_score = max(0.0, min(1.0, llm_score))
    except:
        llm_score = 0.5
    
    # Combine
    return 0.4 * semantic_score + 0.6 * llm_score


def calculate_conciseness(llm: AzureChatOpenAI, question: str, answer: str) -> float:
    """Calculate conciseness score."""
    if not answer or len(answer.strip()) < 10 or "[NO ANSWER]" in answer or "[ERROR]" in answer:
        return 0.0
    
    word_count = len(answer.split())
    sentence_count = len([s for s in answer.split('.') if s.strip()])
    
    prompt = f"""You are evaluating if an answer is appropriately concise.

**Question:**
{question}

**Answer:**
{answer}

**Answer Stats:**
- Word Count: {word_count}
- Sentence Count: {sentence_count}

**Task:**
Rate conciseness from 0 to 1:
- 1.0 = Perfectly concise - contains only necessary information, no fluff
- 0.7 = Slightly verbose but acceptable
- 0.5 = Moderately verbose with some unnecessary content
- 0.3 = Too verbose or too terse
- 0.0 = Extremely verbose or extremely brief (missing key points)

Respond with ONLY a number between 0 and 1 (e.g., 0.85)

**Conciseness Score:**"""

    try:
        response = llm.invoke(prompt)
        score = float(response.content.strip())
        return max(0.0, min(1.0, score))
    except:
        return 0.5


def calculate_uncertainty_detection(answer: str, context: str, ground_truth: str) -> Dict:
    """Calculate uncertainty detection metrics."""
    if not answer or len(answer.strip()) < 10 or "[NO ANSWER]" in answer or "[ERROR]" in answer:
        return {
            'uncertainty_score': 0.0,
            'has_citations': False,
            'uncertainty_phrases': [],
            'confidence_level': 'unknown',
            'appropriate_uncertainty': False
        }
    
    # Uncertainty phrases
    uncertainty_phrases = [
        'based on', 'according to', 'suggests that', 'indicates that',
        'appears to', 'seems to', 'likely', 'probably', 'possibly',
        'may', 'might', 'could', 'approximately', 'around',
        'estimated', 'roughly', 'about', 'generally', 'typically',
        'in most cases', 'often', 'usually', 'tends to',
        'from the context', 'as mentioned', 'as stated'
    ]
    
    # Citation patterns
    citation_patterns = [
        r'\[.*?\]',
        r'\(.*?\)',
        'according to the context',
        'based on the information provided',
        'from the context',
        'the context states',
        'the context mentions'
    ]
    
    # Check for uncertainty phrases
    found_phrases = []
    answer_lower = answer.lower()
    for phrase in uncertainty_phrases:
        if phrase in answer_lower:
            found_phrases.append(phrase)
    
    # Check for citations
    has_citations = any(re.search(pattern, answer, re.IGNORECASE) for pattern in citation_patterns)
    
    # Determine confidence level
    uncertainty_count = len(found_phrases)
    
    if uncertainty_count > 3 or has_citations:
        confidence_level = 'low'
    elif uncertainty_count >= 1:
        confidence_level = 'medium'
    else:
        confidence_level = 'high'
    
    # Check appropriateness
    if context and ground_truth:
        gt_words = set(ground_truth.lower().split())
        ctx_words = set(context.lower().split())
        overlap = len(gt_words.intersection(ctx_words)) / len(gt_words) if gt_words else 0
        context_completeness = overlap
    else:
        context_completeness = 0.5
    
    # Score appropriateness
    if context_completeness > 0.8:
        appropriate = confidence_level in ['high', 'medium']
        score = 1.0 if appropriate else 0.5
    elif context_completeness > 0.5:
        appropriate = confidence_level in ['medium', 'low']
        score = 1.0 if appropriate else 0.6
    else:
        appropriate = confidence_level == 'low'
        score = 1.0 if appropriate else 0.3
    
    return {
        'uncertainty_score': score,
        'has_citations': has_citations,
        'uncertainty_phrases': found_phrases[:5],
        'confidence_level': confidence_level,
        'appropriate_uncertainty': score >= 0.7
    }


# ============================================================================
# EVALUATION FUNCTION
# ============================================================================

def evaluate_single_method(llm, embeddings, row: pd.Series, method: str) -> Dict:
    """
    Evaluate one RAG method with all metrics.
    Uses REAL latency and token data from enhanced evaluation.
    """
    
    question = row['question']
    ground_truth = row['ground_truth_answer']
    context = row[f'{method}_context']
    answer = row[f'{method}_answer']
    
    print(f"   Evaluating {method.upper()}...")
    
    # Calculate quality metrics
    faithfulness = calculate_faithfulness(llm, context, answer)
    relevance = calculate_answer_relevance(llm, question, answer)
    precision = calculate_context_precision(llm, question, context)
    recall = calculate_context_recall(llm, ground_truth, context)
    correctness = calculate_correctness(embeddings, llm, ground_truth, answer)
    conciseness = calculate_conciseness(llm, question, answer)
    uncertainty_metrics = calculate_uncertainty_detection(answer, context, ground_truth)
    
    # Get REAL metrics from evaluation
    retrieval_latency = row[f'{method}_retrieval_latency_sec']
    generation_latency = row[f'{method}_generation_latency_sec']
    total_latency = row[f'{method}_total_latency_sec']
    
    context_tokens = row[f'{method}_context_tokens']
    answer_tokens = row[f'{method}_answer_tokens']
    input_tokens = row[f'{method}_input_tokens']
    output_tokens = row[f'{method}_output_tokens']
    total_tokens = row[f'{method}_total_tokens']
    
    generation_cost = row[f'{method}_cost_inr']
    
    # Compile metrics
    metrics = {
        'question_id': row['question_id'],
        'method': method,
        
        # Quality metrics (7)
        'faithfulness': faithfulness,
        'answer_relevance': relevance,
        'context_precision': precision,
        'context_recall': recall,
        'correctness': correctness,
        'conciseness': conciseness,
        'uncertainty_score': uncertainty_metrics['uncertainty_score'],
        
        # Latency (REAL from evaluation)
        'retrieval_latency_sec': retrieval_latency,
        'generation_latency_sec': generation_latency,
        'total_latency_sec': total_latency,
        
        # Tokens (REAL from evaluation)
        'context_tokens': context_tokens,
        'answer_tokens': answer_tokens,
        'input_tokens': input_tokens,
        'output_tokens': output_tokens,
        'total_tokens': total_tokens,
        
        # Cost (REAL from evaluation)
        'generation_cost_inr': generation_cost,
        'total_cost_inr': generation_cost,
        
        # Uncertainty details
        'has_citations': uncertainty_metrics['has_citations'],
        'confidence_level': uncertainty_metrics['confidence_level'],
        'appropriate_uncertainty': uncertainty_metrics['appropriate_uncertainty'],
        
        # Word counts
        'answer_word_count': len(answer.split()) if answer else 0,
        'context_word_count': len(context.split()) if context else 0
    }
    
    # Calculate overall score (7 quality metrics)
    metric_values = [
        metrics['faithfulness'],
        metrics['answer_relevance'],
        metrics['context_precision'],
        metrics['context_recall'],
        metrics['correctness'],
        metrics['conciseness'],
        metrics['uncertainty_score']
    ]
    metrics['overall_score'] = np.mean(metric_values)
    
    # Print summary
    print(f"      Faithfulness: {metrics['faithfulness']:.3f}")
    print(f"      Answer Relevance: {metrics['answer_relevance']:.3f}")
    print(f"      Context Precision: {metrics['context_precision']:.3f}")
    print(f"      Context Recall: {metrics['context_recall']:.3f}")
    print(f"      Correctness: {metrics['correctness']:.3f}")
    print(f"      Conciseness: {metrics['conciseness']:.3f} 📏")
    print(f"      Uncertainty: {metrics['uncertainty_score']:.3f} 🎯")
    print(f"      → Overall: {metrics['overall_score']:.3f}")
    print(f"      Latency: {metrics['total_latency_sec']:.2f}s (Retrieval: {metrics['retrieval_latency_sec']:.2f}s + Generation: {metrics['generation_latency_sec']:.2f}s)")
    print(f"      Cost: ₹{metrics['total_cost_inr']:.4f} ({metrics['total_tokens']} tokens)")
    
    return metrics


def main():
    """Main evaluation function."""
    
    print("=" * 80)
    print("📊 FINAL RAG METRICS CALCULATION")
    print("=" * 80)
    print("Uses REAL latency, tokens, and costs from enhanced evaluation")
    print("Calculates: 7 Quality Metrics + Conciseness + Uncertainty")
    print("=" * 80)
    
    # Load enhanced results
    print("\n📂 Loading enhanced evaluation results...")
    try:
        df = pd.read_csv(RESULTS_PATH)
        print(f"✅ Loaded {len(df)} questions with real metrics")
    except FileNotFoundError:
        print(f"❌ Enhanced results not found!")
        print(f"   Expected: {RESULTS_PATH}")
        print(f"   Please run 'evaluate_rag_enhanced.py' first!")
        return
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        return
    
    # Initialize LLM and embeddings
    print("\n🤖 Initializing Azure OpenAI...")
    llm = initialize_llm()
    embeddings = initialize_embeddings()
    print("✅ LLM and embeddings ready")
    
    # Calculate metrics
    print(f"\n🔄 Calculating quality metrics for {len(df)} questions...")
    
    all_metrics = []
    
    for idx, row in df.iterrows():
        print(f"\n[{idx+1}/{len(df)}] {row['question_id']}: {row['question'][:60]}...")
        
        # Evaluate each method
        for method in ['local', 'global', 'faiss']:
            metrics = evaluate_single_method(llm, embeddings, row, method)
            all_metrics.append(metrics)
    
    # Convert to DataFrame
    metrics_df = pd.DataFrame(all_metrics)
    
    # Save results
    print(f"\n💾 Saving final metrics...")
    metrics_df.to_csv(METRICS_OUTPUT, index=False)
    print(f"✅ Saved to: {METRICS_OUTPUT}")
    
    # Summary statistics
    print("\n" + "=" * 80)
    print("📊 FINAL METRICS SUMMARY")
    print("=" * 80)
    
    for method in ['local', 'global', 'faiss']:
        method_data = metrics_df[metrics_df['method'] == method]
        
        print(f"\n{method.upper()} Method:")
        print(f"  Quality Metrics:")
        print(f"    Faithfulness:      {method_data['faithfulness'].mean():.3f}")
        print(f"    Answer Relevance:  {method_data['answer_relevance'].mean():.3f}")
        print(f"    Context Precision: {method_data['context_precision'].mean():.3f}")
        print(f"    Context Recall:    {method_data['context_recall'].mean():.3f}")
        print(f"    Correctness:       {method_data['correctness'].mean():.3f}")
        print(f"    Conciseness:       {method_data['conciseness'].mean():.3f} 📏")
        print(f"    Uncertainty:       {method_data['uncertainty_score'].mean():.3f} 🎯")
        print(f"    → Overall Score:   {method_data['overall_score'].mean():.3f}")
        
        print(f"\n  Performance Metrics (REAL):")
        print(f"    Avg Total Latency:     {method_data['total_latency_sec'].mean():.2f}s ⏱️")
        print(f"      - Retrieval:         {method_data['retrieval_latency_sec'].mean():.2f}s")
        print(f"      - Generation:        {method_data['generation_latency_sec'].mean():.2f}s")
        print(f"    Total Cost:            ₹{method_data['total_cost_inr'].sum():.2f} 💰")
        print(f"    Avg Cost per Query:    ₹{method_data['total_cost_inr'].mean():.4f}")
        print(f"    Total Tokens:          {method_data['total_tokens'].sum():.0f}")
        print(f"    Avg Tokens per Query:  {method_data['total_tokens'].mean():.0f}")
    
    # Grand totals
    print("\n" + "=" * 80)
    print("💰 GRAND TOTALS")
    print("=" * 80)
    print(f"Total Cost: ₹{metrics_df['total_cost_inr'].sum():.2f}")
    print(f"Total Tokens: {metrics_df['total_tokens'].sum():.0f}")
    print(f"Total Questions: {len(df)}")
    print(f"Average Cost per Question: ₹{metrics_df.groupby(metrics_df.index // 3)['total_cost_inr'].sum().mean():.4f}")
    
    print("\n" + "=" * 80)
    print("✅ FINAL METRICS CALCULATION COMPLETE!")
    print("=" * 80)
    
    return metrics_df


if __name__ == "__main__":
    main()