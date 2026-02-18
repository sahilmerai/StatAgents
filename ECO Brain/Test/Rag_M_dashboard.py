# Rag_M_dashboard_enhanced.py
"""
Enhanced DOE RAG Dashboard with Improved Visuals and LaTeX Support
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import numpy as np
import re

st.set_page_config(
    page_title="Enhanced DOE RAG Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for better visuals
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .quality-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .performance-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .answer-box {
        background-color: #ffffff;
        border-left: 4px solid #4CAF50;
        padding: 20px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        font-size: 16px;
        line-height: 1.8;
    }
    .context-box {
        background-color: #fff9e6;
        border-left: 4px solid #FFC107;
        padding: 20px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        font-size: 14px;
        line-height: 1.6;
    }
    .ground-truth-box {
        background-color: #e8f5e9;
        border-left: 4px solid #4CAF50;
        padding: 20px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        font-size: 15px;
        line-height: 1.7;
    }
    .question-box {
        background-color: #e3f2fd;
        border-left: 4px solid #2196F3;
        padding: 20px;
        border-radius: 5px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        font-size: 17px;
        font-weight: 500;
        line-height: 1.6;
    }
    .method-comparison {
        background-color: #f5f5f5;
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    .metric-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
    }
    .badge-excellent {
        background-color: #4CAF50;
        color: white;
    }
    .badge-good {
        background-color: #FFC107;
        color: black;
    }
    .badge-fair {
        background-color: #FF9800;
        color: white;
    }
    .badge-poor {
        background-color: #f44336;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

RESULTS_DIR = Path(r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\DOE Test\Results")
COMBINED_RESULTS = RESULTS_DIR / "combined_all_results_enhanced.csv"
METRICS_RESULTS = RESULTS_DIR / "metrics_results_final.csv"

@st.cache_data
def load_data():
    combined_df = pd.read_csv(COMBINED_RESULTS)
    metrics_df = pd.read_csv(METRICS_RESULTS)
    return combined_df, metrics_df

def render_latex_text(text):
    """
    Render text with LaTeX formula support.
    Detects formulas and renders them properly.
    """
    # Common DOE patterns to render as LaTeX
    text = re.sub(r'\bn\^k\b', r'$n^k$', text)  # n^k
    text = re.sub(r'\b2\^k\b', r'$2^k$', text)  # 2^k
    text = re.sub(r'(\w+)\^(\d+)', r'$\1^{\2}$', text)  # general powers
    text = re.sub(r'α\s*=\s*([\d.]+)', r'$\\alpha = \1$', text)  # alpha
    text = re.sub(r'β\s*=\s*([\d.]+)', r'$\\beta = \1$', text)  # beta
    text = re.sub(r'μ', r'$\\mu$', text)  # mu
    text = re.sub(r'σ', r'$\\sigma$', text)  # sigma
    
    return text

def get_score_badge(score):
    """Return HTML badge based on score."""
    if score >= 0.8:
        return '<span class="metric-badge badge-excellent">Excellent</span>'
    elif score >= 0.6:
        return '<span class="metric-badge badge-good">Good</span>'
    elif score >= 0.4:
        return '<span class="metric-badge badge-fair">Fair</span>'
    else:
        return '<span class="metric-badge badge-poor">Poor</span>'

def render_sidebar(combined_df):
    st.sidebar.title("📊 Enhanced RAG Evaluation")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio(
        "📍 Navigation",
        [
            "📈 Overview & Quality",
            "💰 Cost & Performance",
            "🔍 Detailed Review",
            "⚖️ Side-by-Side",
            "📊 Export & Reports"
        ],
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("📋 Dataset Info")
    st.sidebar.metric("Total Questions", len(combined_df))
    st.sidebar.metric("Methods Evaluated", 3)
    
    return page

def page_overview(combined_df, metrics_df):
    st.title("📈 Overview & Quality Metrics")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Questions", len(combined_df))
    
    with col2:
        best_method = metrics_df.groupby('method')['overall_score'].mean().idxmax()
        best_score = metrics_df.groupby('method')['overall_score'].mean().max()
        st.metric("Best Quality", best_method.upper(), f"{best_score:.3f}")
    
    with col3:
        cheapest_method = metrics_df.groupby('method')['total_cost_inr'].mean().idxmin()
        cheapest_cost = metrics_df.groupby('method')['total_cost_inr'].mean().min()
        st.metric("Most Economical", cheapest_method.upper(), f"₹{cheapest_cost:.4f}")
    
    with col4:
        fastest_method = metrics_df.groupby('method')['total_latency_sec'].mean().idxmin()
        fastest_time = metrics_df.groupby('method')['total_latency_sec'].mean().min()
        st.metric("Fastest", fastest_method.upper(), f"{fastest_time:.2f}s")
    
    st.markdown("---")
    st.subheader("🎯 Overall Quality Scores")
    
    col1, col2, col3 = st.columns(3)
    
    for (method, name), col in zip(
        [('local', 'GraphRAG Local'), ('global', 'GraphRAG Global'), ('faiss', 'FAISS RAG')],
        [col1, col2, col3]
    ):
        method_data = metrics_df[metrics_df['method'] == method]
        overall = method_data['overall_score'].mean()
        
        with col:
            st.markdown(f"### {name}")
            st.progress(overall)
            st.metric("Score", f"{overall:.3f}")
            
            with st.expander("View Metrics"):
                st.write(f"Faithfulness: {method_data['faithfulness'].mean():.3f}")
                st.write(f"Relevance: {method_data['answer_relevance'].mean():.3f}")
                st.write(f"Precision: {method_data['context_precision'].mean():.3f}")
                st.write(f"Recall: {method_data['context_recall'].mean():.3f}")
                st.write(f"Correctness: {method_data['correctness'].mean():.3f}")
                st.write(f"Conciseness: {method_data['conciseness'].mean():.3f}")
                st.write(f"Uncertainty: {method_data['uncertainty_score'].mean():.3f}")
    
    st.markdown("---")
    st.subheader("📊 Metrics Comparison")
    
    metrics_cols = ['faithfulness', 'answer_relevance', 'context_precision', 
                   'context_recall', 'correctness', 'conciseness', 'uncertainty_score']
    
    comparison_data = []
    for method in ['local', 'global', 'faiss']:
        method_data = metrics_df[metrics_df['method'] == method]
        for metric in metrics_cols:
            comparison_data.append({
                'Method': method.upper(),
                'Metric': metric.replace('_', ' ').title(),
                'Score': method_data[metric].mean()
            })
    
    comparison_df = pd.DataFrame(comparison_data)
    
    fig = px.bar(
        comparison_df,
        x='Metric',
        y='Score',
        color='Method',
        barmode='group',
        title="All 7 Quality Metrics",
        height=450
    )
    fig.update_layout(yaxis_range=[0, 1], xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

def page_cost_performance(combined_df, metrics_df):
    st.title("💰 Cost & Performance")
    st.markdown("---")
    
    st.subheader("⚡ Performance Overview")
    
    col1, col2, col3 = st.columns(3)
    
    for (method, name), col in zip(
        [('local', 'Local'), ('global', 'Global'), ('faiss', 'FAISS')],
        [col1, col2, col3]
    ):
        method_data = metrics_df[metrics_df['method'] == method]
        
        with col:
            st.markdown(f"### {name}")
            st.metric("Latency", f"{method_data['total_latency_sec'].mean():.2f}s")
            st.metric("Cost", f"₹{method_data['total_cost_inr'].mean():.4f}")
            st.metric("Tokens", f"{method_data['total_tokens'].mean():.0f}")
    
    st.markdown("---")
    st.subheader("⏱️ Latency Analysis")
    
    latency_data = []
    for method in ['local', 'global', 'faiss']:
        method_data = metrics_df[metrics_df['method'] == method]
        for _, row in method_data.iterrows():
            latency_data.append({
                'Method': method.upper(),
                'Total (s)': row['total_latency_sec']
            })
    
    latency_df = pd.DataFrame(latency_data)
    
    fig = px.box(
        latency_df,
        x='Method',
        y='Total (s)',
        color='Method',
        title="Latency Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("💰 Cost Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        cost_data = []
        for method in ['local', 'global', 'faiss']:
            method_data = metrics_df[metrics_df['method'] == method]
            cost_data.append({
                'Method': method.upper(),
                'Total Cost (₹)': method_data['total_cost_inr'].sum()
            })
        
        cost_df = pd.DataFrame(cost_data)
        
        fig = px.bar(
            cost_df,
            x='Method',
            y='Total Cost (₹)',
            color='Method',
            title="Total Cost by Method",
            text='Total Cost (₹)'
        )
        fig.update_traces(texttemplate='₹%{text:.4f}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        token_data = []
        for method in ['local', 'global', 'faiss']:
            method_data = metrics_df[metrics_df['method'] == method]
            token_data.extend([
                {'Method': method.upper(), 'Type': 'Context', 'Tokens': method_data['context_tokens'].mean()},
                {'Method': method.upper(), 'Type': 'Answer', 'Tokens': method_data['answer_tokens'].mean()}
            ])
        
        token_df = pd.DataFrame(token_data)
        
        fig = px.bar(
            token_df,
            x='Method',
            y='Tokens',
            color='Type',
            title="Token Usage",
            barmode='stack'
        )
        st.plotly_chart(fig, use_container_width=True)

def page_detailed_review(combined_df, metrics_df):
    """Enhanced Detailed Review with better visuals and LaTeX support."""
    st.title("🔍 Detailed Question Review")
    st.markdown("Enhanced visualization with LaTeX formula support")
    
    st.markdown("---")
    
    question_ids = list(combined_df['question_id'].unique())
    
    if len(question_ids) == 1:
        selected_q = question_ids[0]
        st.info(f"📌 Viewing: **{selected_q}**")
    else:
        selected_q = st.selectbox(
            "Select Question",
            question_ids,
            format_func=lambda x: f"{x} - {combined_df[combined_df['question_id']==x]['question'].iloc[0][:60]}..."
        )
    
    q_data = combined_df[combined_df['question_id'] == selected_q].iloc[0]
    q_metrics = metrics_df[metrics_df['question_id'] == selected_q]
    
    # Question metadata
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📋 Type", q_data['question_type'].title())
    with col2:
        st.metric("⚙️ Complexity", q_data['complexity'].title())
    with col3:
        st.metric("📚 Topic", q_data['topic'])
    
    st.markdown("---")
    
    # Question with LaTeX support
    st.markdown("### ❓ Question")
    question_text = render_latex_text(q_data['question'])
    st.markdown(f'<div class="question-box">{question_text}</div>', unsafe_allow_html=True)
    
    # Ground Truth with LaTeX support
    st.markdown("### ✅ Ground Truth Answer")
    ground_truth_text = render_latex_text(q_data['ground_truth_answer'])
    st.markdown(f'<div class="ground-truth-box">{ground_truth_text}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Method tabs with enhanced visuals
    tab1, tab2, tab3 = st.tabs(["📚 GraphRAG Local", "🌐 GraphRAG Global", "📖 FAISS RAG"])
    
    for tab, method, method_name, emoji, color in zip(
        [tab1, tab2, tab3],
        ['local', 'global', 'faiss'],
        ['GraphRAG Local', 'GraphRAG Global', 'FAISS RAG'],
        ['📚', '🌐', '📖'],
        ['#1f77b4', '#ff7f0e', '#2ca02c']
    ):
        with tab:
            method_metrics = q_metrics[q_metrics['method'] == method].iloc[0]
            
            # Header with overall score
            st.markdown(f"## {emoji} {method_name}")
            
            overall = method_metrics['overall_score']
            badge_html = get_score_badge(overall)
            st.markdown(f"### Overall Score: {overall:.3f} {badge_html}", unsafe_allow_html=True)
            
            st.progress(overall)
            
            st.markdown("---")
            
            # Metrics Dashboard
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown('<div class="quality-section">', unsafe_allow_html=True)
                st.markdown("#### 🎯 Quality Metrics")
                
                quality_metrics = {
                    'Faithfulness': method_metrics['faithfulness'],
                    'Relevance': method_metrics['answer_relevance'],
                    'Precision': method_metrics['context_precision'],
                    'Recall': method_metrics['context_recall'],
                    'Correctness': method_metrics['correctness'],
                    'Conciseness 📏': method_metrics['conciseness'],
                    'Uncertainty 🎯': method_metrics['uncertainty_score']
                }
                
                for metric_name, score in quality_metrics.items():
                    emoji_score = "🟢" if score >= 0.8 else "🟡" if score >= 0.6 else "🟠" if score >= 0.4 else "🔴"
                    st.write(f"{emoji_score} **{metric_name}:** {score:.3f}")
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="performance-section">', unsafe_allow_html=True)
                st.markdown("#### ⚡ Performance Metrics")
                
                # Latency breakdown
                st.write(f"⏱️ **Total Latency:** {method_metrics['total_latency_sec']:.2f}s")
                st.write(f"   • Retrieval: {method_metrics['retrieval_latency_sec']:.2f}s")
                st.write(f"   • Generation: {method_metrics['generation_latency_sec']:.2f}s")
                
                st.write(f"💰 **Total Cost:** ₹{method_metrics['total_cost_inr']:.4f}")
                st.write(f"📊 **Total Tokens:** {method_metrics['total_tokens']:.0f}")
                st.write(f"   • Context: {method_metrics['context_tokens']:.0f}")
                st.write(f"   • Answer: {method_metrics['answer_tokens']:.0f}")
                
                st.markdown("**🎯 Uncertainty Analysis:**")
                st.write(f"   • Confidence: **{method_metrics['confidence_level'].title()}**")
                st.write(f"   • Citations: {'✅ Yes' if method_metrics['has_citations'] else '❌ No'}")
                st.write(f"   • Appropriate: {'✅ Yes' if method_metrics['appropriate_uncertainty'] else '⚠️ No'}")
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Retrieved Context with LaTeX
            st.markdown("### 📥 Retrieved Context")
            context = q_data[f'{method}_context']
            
            if any(x in context for x in ["❌", "⏱️", "⚠️"]):
                st.error(context)
            else:
                context_rendered = render_latex_text(context)
                st.markdown(f'<div class="context-box">{context_rendered}</div>', unsafe_allow_html=True)
                
                with st.expander("📄 View Full Context (Plain Text)"):
                    st.text_area("", context, height=300, key=f"{method}_ctx", label_visibility="collapsed")
            
            st.markdown("---")
            
            # Generated Answer with LaTeX
            st.markdown("### 💬 Generated Answer")
            answer = q_data[f'{method}_answer']
            
            if "[NO ANSWER]" in answer or "[ERROR]" in answer:
                st.error(answer)
            else:
                answer_rendered = render_latex_text(answer)
                st.markdown(f'<div class="answer-box">{answer_rendered}</div>', unsafe_allow_html=True)
                
                # Answer statistics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("📝 Word Count", f"{method_metrics['answer_word_count']:.0f}")
                with col2:
                    st.metric("📊 Tokens", f"{method_metrics['answer_tokens']:.0f}")
                with col3:
                    conciseness_emoji = "🟢" if method_metrics['conciseness'] >= 0.8 else "🟡" if method_metrics['conciseness'] >= 0.6 else "🔴"
                    st.metric("📏 Conciseness", f"{method_metrics['conciseness']:.3f} {conciseness_emoji}")

def page_side_by_side(combined_df, metrics_df):
    """Enhanced Side-by-Side with better visuals and LaTeX support."""
    st.title("⚖️ Side-by-Side Comparison")
    st.markdown("Compare all methods with enhanced visualization")
    
    st.markdown("---")
    
    question_ids = list(combined_df['question_id'].unique())
    
    if len(question_ids) == 1:
        selected_q = question_ids[0]
        st.info(f"📌 Viewing: **{selected_q}**")
    else:
        selected_q = st.selectbox("Select Question", question_ids, key="sbs")
    
    q_data = combined_df[combined_df['question_id'] == selected_q].iloc[0]
    q_metrics = metrics_df[metrics_df['question_id'] == selected_q]
    
    # Question with LaTeX
    st.markdown("### ❓ Question")
    question_text = render_latex_text(q_data['question'])
    st.markdown(f'<div class="question-box">{question_text}</div>', unsafe_allow_html=True)
    
    # Ground Truth with LaTeX
    st.markdown("### ✅ Ground Truth Answer")
    ground_truth_text = render_latex_text(q_data['ground_truth_answer'])
    st.markdown(f'<div class="ground-truth-box">{ground_truth_text}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## 🔬 Three-Way Comparison")
    
    # Three columns for comparison
    col1, col2, col3 = st.columns(3)
    
    for col, method, method_name, emoji, color in zip(
        [col1, col2, col3],
        ['local', 'global', 'faiss'],
        ['GraphRAG Local', 'GraphRAG Global', 'FAISS RAG'],
        ['📚', '🌐', '📖'],
        ['#1f77b4', '#ff7f0e', '#2ca02c']
    ):
        with col:
            method_metrics = q_metrics[q_metrics['method'] == method].iloc[0]
            
            # Method header
            st.markdown(f"### {emoji} {method_name}")
            
            # Overall score
            overall = method_metrics['overall_score']
            badge_html = get_score_badge(overall)
            st.markdown(f"**Overall:** {overall:.3f}")
            st.markdown(badge_html, unsafe_allow_html=True)
            st.progress(overall)
            
            st.markdown("---")
            
            # Performance metrics
            st.markdown("**⚡ Performance:**")
            st.write(f"⏱️ {method_metrics['total_latency_sec']:.2f}s")
            st.write(f"💰 ₹{method_metrics['total_cost_inr']:.4f}")
            st.write(f"📊 {method_metrics['total_tokens']:.0f} tokens")
            
            st.markdown("---")
            
            # Key quality metrics
            with st.expander("🎯 Quality Metrics"):
                st.write(f"**Faithfulness:** {method_metrics['faithfulness']:.3f}")
                st.write(f"**Correctness:** {method_metrics['correctness']:.3f}")
                st.write(f"**Conciseness:** {method_metrics['conciseness']:.3f}")
                st.write(f"**Uncertainty:** {method_metrics['uncertainty_score']:.3f}")
            
            st.markdown("---")
            
            # Answer with LaTeX
            st.markdown("**💬 Answer:**")
            answer = q_data[f'{method}_answer']
            
            if "[NO ANSWER]" in answer or "[ERROR]" in answer:
                st.error(answer[:100] + "...")
            else:
                answer_rendered = render_latex_text(answer)
                # Show preview
                if len(answer) > 200:
                    preview = answer[:200] + "..."
                    preview_rendered = render_latex_text(preview)
                    st.markdown(f'<div style="font-size:14px; padding:10px; background:#f9f9f9; border-radius:5px;">{preview_rendered}</div>', unsafe_allow_html=True)
                    
                    with st.expander("📖 View Full Answer"):
                        st.markdown(f'<div class="answer-box">{answer_rendered}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div style="font-size:14px; padding:10px; background:#f9f9f9; border-radius:5px;">{answer_rendered}</div>', unsafe_allow_html=True)

def page_export(combined_df, metrics_df):
    st.title("📊 Export & Reports")
    st.markdown("---")
    
    st.subheader("📥 Download")
    
    col1, col2 = st.columns(2)
    
    with col1:
        csv1 = combined_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "⬇️ Evaluation Results",
            csv1,
            "evaluation_results.csv",
            "text/csv"
        )
    
    with col2:
        csv2 = metrics_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "⬇️ Metrics",
            csv2,
            "metrics.csv",
            "text/csv"
        )
    
    st.markdown("---")
    st.subheader("📝 Summary Report")
    
    best_quality = metrics_df.groupby('method')['overall_score'].mean().idxmax()
    best_score = metrics_df.groupby('method')['overall_score'].mean().max()
    
    cheapest = metrics_df.groupby('method')['total_cost_inr'].mean().idxmin()
    cheapest_cost = metrics_df.groupby('method')['total_cost_inr'].mean().min()
    
    fastest = metrics_df.groupby('method')['total_latency_sec'].mean().idxmin()
    fastest_time = metrics_df.groupby('method')['total_latency_sec'].mean().min()
    
    report = f"""
# RAG Evaluation Report

## Summary
- Total Questions: {len(combined_df)}
- Best Quality: {best_quality.upper()} ({best_score:.3f})
- Most Economical: {cheapest.upper()} (₹{cheapest_cost:.4f})
- Fastest: {fastest.upper()} ({fastest_time:.2f}s)

## Detailed Results
"""
    
    for method in ['local', 'global', 'faiss']:
        method_data = metrics_df[metrics_df['method'] == method]
        report += f"""
### {method.upper()}
- Overall Score: {method_data['overall_score'].mean():.3f}
- Faithfulness: {method_data['faithfulness'].mean():.3f}
- Relevance: {method_data['answer_relevance'].mean():.3f}
- Precision: {method_data['context_precision'].mean():.3f}
- Recall: {method_data['context_recall'].mean():.3f}
- Correctness: {method_data['correctness'].mean():.3f}
- Conciseness: {method_data['conciseness'].mean():.3f}
- Uncertainty: {method_data['uncertainty_score'].mean():.3f}
- Avg Latency: {method_data['total_latency_sec'].mean():.2f}s
- Total Cost: ₹{method_data['total_cost_inr'].sum():.2f}
- Avg Tokens: {method_data['total_tokens'].mean():.0f}
"""
    
    st.markdown(report)
    
    st.download_button(
        "⬇️ Download Report",
        report.encode('utf-8'),
        "report.md",
        "text/markdown"
    )

def main():
    try:
        combined_df, metrics_df = load_data()
    except FileNotFoundError:
        st.error("❌ Files not found! Run evaluate_rag_enhanced.py and calculate_metrics_v3.py first.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.stop()
    
    page = render_sidebar(combined_df)
    
    if page == "📈 Overview & Quality":
        page_overview(combined_df, metrics_df)
    elif page == "💰 Cost & Performance":
        page_cost_performance(combined_df, metrics_df)
    elif page == "🔍 Detailed Review":
        page_detailed_review(combined_df, metrics_df)
    elif page == "⚖️ Side-by-Side":
        page_side_by_side(combined_df, metrics_df)
    elif page == "📊 Export & Reports":
        page_export(combined_df, metrics_df)

if __name__ == "__main__":
    main()