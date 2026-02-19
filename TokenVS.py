# TokenVS.py - Token Tracking Visualization & Analysis Dashboard
"""
Comprehensive dashboard for analyzing multi-agent token consumption,
costs, performance, and routing patterns across sessions.
"""

import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
from datetime import datetime
import numpy as np

# Try importing networkx, show warning if not available
try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False
    st.warning("⚠️ NetworkX not installed. Network graphs will not be available. Install with: pip install networkx")

# Page config
st.set_page_config(
    page_title="Token Tracking Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

@st.cache_data(ttl=5)  # Cache for 5 seconds for live refresh
def load_available_sessions(base_dir="./Token"):
    """Load all available experiment sessions"""
    base_path = Path(base_dir)
    if not base_path.exists():
        return []
    
    experiments = sorted(
        [d for d in base_path.iterdir() if d.is_dir() and d.name.startswith("Experiment_")],
        key=lambda x: x.name,
        reverse=True  # Most recent first
    )
    
    return [exp.name for exp in experiments]


@st.cache_data
def load_session_data(session_name, base_dir="./Token"):
    """Load all data files for a session"""
    session_path = Path(base_dir) / session_name
    
    if not session_path.exists():
        return None
    
    data = {
        'session_name': session_name,
        'session_path': str(session_path)
    }
    
    # Load CSV files
    csv_files = [
        'session_summary.csv',
        'agent_performance.csv',
        'tool_analytics.csv',
        'routing_data.csv',
        'system_prompts_tracking.csv',
        'system_prompts_summary.csv'
    ]
    
    for csv_file in csv_files:
        file_path = session_path / csv_file
        if file_path.exists():
            try:
                df = pd.read_csv(file_path)
                key = csv_file.replace('.csv', '')
                data[key] = df
            except Exception as e:
                st.warning(f"Error loading {csv_file}: {str(e)}")
    
    # Load JSON files
    json_files = ['detailed_log.json', 'routing_data.json']
    for json_file in json_files:
        file_path = session_path / json_file
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                key = json_file.replace('.json', '_json')
                data[key] = json_data
            except Exception as e:
                st.warning(f"Error loading {json_file}: {str(e)}")
    
    # Load text files
    txt_files = ['conversation_flow.txt', 'system_prompts_full.txt']
    for txt_file in txt_files:
        file_path = session_path / txt_file
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    txt_data = f.read()
                key = txt_file.replace('.txt', '_txt')
                data[key] = txt_data
            except Exception as e:
                st.warning(f"Error loading {txt_file}: {str(e)}")
    
    return data


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_cost_breakdown_chart(session_data):
    """Create pie chart for cost breakdown"""
    summary = session_data.get('session_summary')
    if summary is None or summary.empty:
        return None
    
    row = summary.iloc[0]
    
    fig = go.Figure(data=[go.Pie(
        labels=['System Prompts', 'Conversation'],
        values=[row['system_prompt_cost_inr'], row['conversation_cost_inr']],
        hole=0.4,
        marker=dict(colors=['#667eea', '#764ba2']),
        textinfo='label+percent+value',
        texttemplate='%{label}<br>₹%{value:.2f}<br>(%{percent})'
    )])
    
    fig.update_layout(
        title=f"Cost Breakdown - Total: ₹{row['total_cost_inr']:.2f}",
        height=400,
        showlegend=True
    )
    
    return fig


def create_agent_performance_chart(session_data):
    """Create bar chart for agent performance"""
    agent_perf = session_data.get('agent_performance')
    if agent_perf is None or agent_perf.empty:
        return None
    
    fig = go.Figure()
    
    # System prompt costs
    fig.add_trace(go.Bar(
        name='System Prompts',
        x=agent_perf['agent_name'],
        y=agent_perf['system_prompt_cost_inr'],
        marker_color='#667eea',
        text=agent_perf['system_prompt_cost_inr'].apply(lambda x: f'₹{x:.2f}'),
        textposition='inside'
    ))
    
    # Conversation costs
    fig.add_trace(go.Bar(
        name='Conversation',
        x=agent_perf['agent_name'],
        y=agent_perf['conversation_cost_inr'],
        marker_color='#764ba2',
        text=agent_perf['conversation_cost_inr'].apply(lambda x: f'₹{x:.2f}'),
        textposition='inside'
    ))
    
    fig.update_layout(
        title="Agent Cost Breakdown",
        xaxis_title="Agent",
        yaxis_title="Cost (INR)",
        barmode='stack',
        height=400,
        showlegend=True
    )
    
    return fig


def create_routing_sankey(session_data):
    """Create Sankey diagram for agent routing"""
    routing = session_data.get('routing_data')
    if routing is None or routing.empty:
        return None
    
    # Get unique agents
    all_agents = list(set(routing['from_agent'].tolist() + routing['to_agent'].tolist()))
    agent_to_idx = {agent: idx for idx, agent in enumerate(all_agents)}
    
    # Create Sankey data
    source = [agent_to_idx[agent] for agent in routing['from_agent']]
    target = [agent_to_idx[agent] for agent in routing['to_agent']]
    value = routing['handoff_count'].tolist()
    
    # Colors
    colors = px.colors.qualitative.Set3
    link_colors = [colors[i % len(colors)] for i in source]
    
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=all_agents,
            color=[colors[i % len(colors)] for i in range(len(all_agents))]
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors
        )
    )])
    
    fig.update_layout(
        title="Agent Routing Flow",
        height=500,
        font=dict(size=12)
    )
    
    return fig


def create_token_distribution_chart(session_data):
    """Create stacked bar chart for token distribution"""
    agent_perf = session_data.get('agent_performance')
    if agent_perf is None or agent_perf.empty:
        return None
    
    fig = go.Figure()
    
    # System prompt tokens
    fig.add_trace(go.Bar(
        name='System Prompts',
        x=agent_perf['agent_name'],
        y=agent_perf['system_prompt_tokens'],
        marker_color='#667eea'
    ))
    
    # Conversation input
    fig.add_trace(go.Bar(
        name='Input',
        x=agent_perf['agent_name'],
        y=agent_perf['conversation_input_tokens'],
        marker_color='#48bb78'
    ))
    
    # Conversation output
    fig.add_trace(go.Bar(
        name='Output',
        x=agent_perf['agent_name'],
        y=agent_perf['conversation_output_tokens'],
        marker_color='#f56565'
    ))
    
    fig.update_layout(
        title="Token Distribution by Agent",
        xaxis_title="Agent",
        yaxis_title="Tokens",
        barmode='stack',
        height=400
    )
    
    return fig


def create_tool_usage_chart(session_data):
    """Create horizontal bar chart for tool usage"""
    tool_analytics = session_data.get('tool_analytics')
    if tool_analytics is None or tool_analytics.empty:
        return None
    
    # Sort by call count
    tool_analytics_sorted = tool_analytics.sort_values('call_count', ascending=True)
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=tool_analytics_sorted['tool_name'],
        x=tool_analytics_sorted['call_count'],
        orientation='h',
        marker_color='#764ba2',
        text=tool_analytics_sorted['call_count'],
        textposition='inside'
    ))
    
    fig.update_layout(
        title="Tool Usage Frequency",
        xaxis_title="Number of Calls",
        yaxis_title="Tool",
        height=max(300, len(tool_analytics_sorted) * 40)
    )
    
    return fig


def create_system_prompt_loads_chart(session_data):
    """Create timeline of system prompt loads"""
    sp_tracking = session_data.get('system_prompts_tracking')
    if sp_tracking is None or sp_tracking.empty:
        return None
    
    # Convert timestamp to datetime
    sp_tracking['timestamp'] = pd.to_datetime(sp_tracking['timestamp'])
    
    fig = px.scatter(
        sp_tracking,
        x='timestamp',
        y='agent_name',
        size='tokens',
        color='agent_name',
        hover_data=['tokens', 'cost_inr', 'load_number'],
        title="System Prompt Load Timeline"
    )
    
    fig.update_layout(
        height=400,
        xaxis_title="Time",
        yaxis_title="Agent",
        showlegend=False
    )
    
    return fig


# ============================================================================
# SIDEBAR - SESSION SELECTOR
# ============================================================================

with st.sidebar:
    st.sidebar.image("F:\Project work\Cafe Restaurant Analysis\Agents\StatAgents logo\StatAgents G1.png", use_container_width = True)
    st.title("StatAgents")
    st.markdown("---")
    
    # Live refresh button
    if st.button("🔄 Refresh Sessions", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    
    # Load available sessions
    sessions = load_available_sessions()
    
    if not sessions:
        st.error("No experiment sessions found in ./Token/")
        st.stop()
    
    st.success(f"Found {len(sessions)} sessions")
    
    # Comparison mode toggle
    comparison_mode = st.toggle("Compare Multiple Sessions", value=False)
    
    if comparison_mode:
        st.subheader("Select Sessions to Compare")
        selected_sessions = st.multiselect(
            "Choose 2-3 sessions",
            options=sessions,
            max_selections=3,
            default=[sessions[0]] if sessions else []
        )
    else:
        st.subheader("Select Session")
        selected_session = st.selectbox(
            "Choose experiment",
            options=sessions,
            index=0
        )
        selected_sessions = [selected_session]
    
    st.markdown("---")
    
    # Load data for selected sessions
    session_data_list = []
    for session in selected_sessions:
        data = load_session_data(session)
        if data:
            session_data_list.append(data)
    
    if not session_data_list:
        st.error("Could not load session data")
        st.stop()
    
    # Display session info
    st.subheader("Session Info")
    for idx, data in enumerate(session_data_list):
        with st.expander(f"📁 {data['session_name']}", expanded=(idx == 0)):
            summary = data.get('session_summary')
            if summary is not None and not summary.empty:
                row = summary.iloc[0]
                st.metric("Total Cost", f"₹{row['total_cost_inr']:.2f}")
                st.metric("Total Tokens", f"{row['total_tokens']:,}")
                st.metric("Duration", f"{row['total_execution_time']:.1f}s")
                st.metric("Messages", row['total_messages'])


# ============================================================================
# MAIN CONTENT - TABS
# ============================================================================

# Header
st.title("📊 Token Tracking Analysis Dashboard")

if comparison_mode and len(selected_sessions) > 1:
    st.info(f"Comparing {len(selected_sessions)} sessions: {', '.join(selected_sessions)}")
else:
    st.info(f"Analyzing: {selected_sessions[0]}")

st.markdown("---")

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Overview",
    "🤖 Agent Performance", 
    "🔀 Routing",
    "💬 Session Deep Dive",
    "🛠️ Tool Analytics",
    "💰 Cost Analysis",
    "📂 Raw Data"
])


# ============================================================================
# TAB 1: OVERVIEW DASHBOARD
# ============================================================================

with tab1:
    st.header("Overview Dashboard")
    
    # Use first session for single view, compare for multi-view
    primary_data = session_data_list[0]
    summary = primary_data.get('session_summary')
    
    if summary is not None and not summary.empty:
        row = summary.iloc[0]
        
        # Top KPIs with better visibility
        st.markdown("""
        <style>
        div[data-testid="metric-container"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        div[data-testid="metric-container"] > label {
            color: white !important;
            font-weight: 600 !important;
        }
        div[data-testid="metric-container"] > div {
            color: white !important;
            font-size: 1.8rem !important;
            font-weight: 700 !important;
        }
        div[data-testid="metric-container"] > div > div {
            color: rgba(255,255,255,0.8) !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Cost",
                f"₹{row['total_cost_inr']:.2f}",
                delta=None
            )
        
        with col2:
            st.metric(
                "Total Tokens",
                f"{row['total_tokens']:,}",
                delta=None
            )
        
        with col3:
            st.metric(
                "System Prompts",
                f"₹{row['system_prompt_cost_inr']:.2f}",
                delta=f"{row['system_prompt_tokens']:,} tokens"
            )
        
        with col4:
            st.metric(
                "Conversation",
                f"₹{row['conversation_cost_inr']:.2f}",
                delta=f"{row['conversation_input_tokens'] + row['conversation_output_tokens']:,} tokens"
            )
        
        st.markdown("---")
        
        # Top 3 priority visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # 1. Cost Breakdown
            fig = create_cost_breakdown_chart(primary_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True, key="overview_cost_breakdown")
        
        with col2:
            # 2. Agent Performance
            fig = create_agent_performance_chart(primary_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True, key="overview_agent_performance")
        
        # 3. Routing Sankey (full width)
        st.markdown("### Agent Routing Flow")
        fig = create_routing_sankey(primary_data)
        if fig:
            st.plotly_chart(fig, use_container_width=True, key="overview_routing_sankey")
        
        # Additional: Token Distribution
        st.markdown("### Token Distribution")
        fig = create_token_distribution_chart(primary_data)
        if fig:
            st.plotly_chart(fig, use_container_width=True, key="overview_token_distribution")
    
    else:
        st.error("No session summary data available")


# ============================================================================
# TAB 2: AGENT PERFORMANCE
# ============================================================================

with tab2:
    st.header("Agent Performance Analysis")
    
    primary_data = session_data_list[0]
    agent_perf = primary_data.get('agent_performance')
    
    if agent_perf is not None and not agent_perf.empty:
        
        # Agent selection for drill-down
        selected_agent = st.selectbox(
            "Select agent for detailed view",
            options=agent_perf['agent_name'].tolist(),
            key='agent_selector'
        )
        
        agent_row = agent_perf[agent_perf['agent_name'] == selected_agent].iloc[0]
        
        # Agent metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Call Count", agent_row['call_count'])
        
        with col2:
            st.metric("Total Tokens", f"{agent_row['total_tokens']:,}")
        
        with col3:
            st.metric("Total Cost", f"₹{agent_row['total_cost_inr']:.2f}")
        
        with col4:
            st.metric("Avg Time", f"{agent_row['total_execution_time'] / agent_row['call_count']:.2f}s")
        
        with col5:
            st.metric("Success Rate", f"{agent_row['success_rate']:.1f}%")
        
        st.markdown("---")
        
        # Detailed breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Token Breakdown")
            
            token_data = {
                'Category': ['System Prompts', 'Input', 'Output'],
                'Tokens': [
                    agent_row['system_prompt_tokens'],
                    agent_row['conversation_input_tokens'],
                    agent_row['conversation_output_tokens']
                ]
            }
            
            fig = px.pie(
                token_data,
                values='Tokens',
                names='Category',
                title=f"{selected_agent} - Token Distribution"
            )
            st.plotly_chart(fig, use_container_width=True, key=f"agent_token_pie_{selected_agent}")
        
        with col2:
            st.subheader("Cost Breakdown")
            
            cost_data = {
                'Category': ['System Prompts', 'Conversation'],
                'Cost': [
                    agent_row['system_prompt_cost_inr'],
                    agent_row['conversation_cost_inr']
                ]
            }
            
            fig = px.bar(
                cost_data,
                x='Category',
                y='Cost',
                title=f"{selected_agent} - Cost Analysis",
                color='Category'
            )
            fig.update_yaxes(title="Cost (INR)")
            st.plotly_chart(fig, use_container_width=True, key=f"agent_cost_bar_{selected_agent}")
        
        # System prompt loads
        st.markdown("### System Prompt Load History")
        sp_tracking = primary_data.get('system_prompts_tracking')
        if sp_tracking is not None and not sp_tracking.empty:
            agent_sp = sp_tracking[sp_tracking['agent_name'] == selected_agent]
            if not agent_sp.empty:
                st.dataframe(agent_sp, use_container_width=True)
            else:
                st.info("No system prompt loads for this agent")
        
        # Comparison table (all agents)
        st.markdown("### Agent Comparison")
        
        comparison_df = agent_perf[[
            'agent_name', 'call_count', 'total_tokens', 'total_cost_inr',
            'system_prompt_loads', 'success_rate'
        ]].copy()
        
        comparison_df['total_cost_inr'] = comparison_df['total_cost_inr'].apply(lambda x: f"₹{x:.2f}")
        comparison_df['success_rate'] = comparison_df['success_rate'].apply(lambda x: f"{x:.1f}%")
        
        st.dataframe(comparison_df, use_container_width=True)
    
    else:
        st.error("No agent performance data available")


# ============================================================================
# TAB 3: CONVERSATION ROUTING
# ============================================================================

with tab3:
    st.header("Conversation Routing & Agent Interactions")
    
    primary_data = session_data_list[0]
    routing = primary_data.get('routing_data')
    
    if routing is not None and not routing.empty:
        
        # Summary metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Handoffs", routing['handoff_count'].sum())
        
        with col2:
            st.metric("Unique Routes", len(routing))
        
        with col3:
            most_common = routing.loc[routing['handoff_count'].idxmax()]
            st.metric(
                "Most Common Route",
                f"{most_common['from_agent']} → {most_common['to_agent']}",
                delta=f"{most_common['handoff_count']} times"
            )
        
        st.markdown("---")
        
        # Sankey diagram
        fig = create_routing_sankey(primary_data)
        if fig:
            st.plotly_chart(fig, use_container_width=True, key="routing_sankey_main")
        
        st.markdown("---")
        
        # Routing table
        st.subheader("Routing Details")
        
        routing_display = routing.copy()
        routing_display['total_cost_inr'] = routing_display['total_cost_inr'].apply(lambda x: f"₹{x:.4f}")
        routing_display['avg_tokens'] = routing_display['avg_tokens'].apply(lambda x: f"{x:.1f}")
        
        st.dataframe(routing_display, use_container_width=True)
        
        # Network graph (interactive)
        st.markdown("### Agent Network Graph")
        
        if not NETWORKX_AVAILABLE:
            st.warning("⚠️ Network graph requires NetworkX. Install with: `pip install networkx`")
        else:
            # Create edge list for network
            edge_data = []
            for _, row in routing.iterrows():
                edge_data.append({
                    'source': row['from_agent'],
                    'target': row['to_agent'],
                    'weight': row['handoff_count']
                })
            
            if edge_data:
                # Get unique nodes
                nodes = list(set([e['source'] for e in edge_data] + [e['target'] for e in edge_data]))
                
                # Create network visualization
                G = nx.DiGraph()
                for edge in edge_data:
                    G.add_edge(edge['source'], edge['target'], weight=edge['weight'])
                
                pos = nx.spring_layout(G, k=2, iterations=50)
                
                # Create edge trace
                edge_trace = []
                for edge in G.edges(data=True):
                    x0, y0 = pos[edge[0]]
                    x1, y1 = pos[edge[1]]
                    edge_trace.append(
                        go.Scatter(
                            x=[x0, x1, None],
                            y=[y0, y1, None],
                            mode='lines',
                            line=dict(width=edge[2]['weight'] * 2, color='#888'),
                            hoverinfo='none',
                            showlegend=False
                        )
                    )
                
                # Create node trace
                node_x = []
                node_y = []
                node_text = []
                
                for node in G.nodes():
                    x, y = pos[node]
                    node_x.append(x)
                    node_y.append(y)
                    node_text.append(node)
                
                node_trace = go.Scatter(
                    x=node_x,
                    y=node_y,
                    mode='markers+text',
                    text=node_text,
                    textposition='top center',
                    marker=dict(
                        size=30,
                        color='#764ba2',
                        line=dict(width=2, color='white')
                    ),
                    hoverinfo='text'
                )
                
                # Create figure
                fig = go.Figure(data=edge_trace + [node_trace])
                fig.update_layout(
                    title="Agent Interaction Network",
                    showlegend=False,
                    hovermode='closest',
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    height=600
                )
                
                st.plotly_chart(fig, use_container_width=True, key="routing_network_graph")
    
    else:
        st.info("No routing data available for this session")


# ============================================================================
# TAB 4: SESSION DEEP DIVE
# ============================================================================

with tab4:
    st.header("Session Deep Dive")
    
    primary_data = session_data_list[0]
    
    # Load detailed log
    detailed_log = primary_data.get('detailed_log_json')
    
    if detailed_log and 'messages' in detailed_log:
        messages = detailed_log['messages']
        
        st.subheader(f"Message Timeline ({len(messages)} messages)")
        
        # Create timeline visualization
        df_messages = pd.DataFrame(messages)
        df_messages['timestamp'] = pd.to_datetime(df_messages['timestamp'])
        
        # Message type distribution
        col1, col2 = st.columns(2)
        
        with col1:
            action_counts = df_messages['action_type'].value_counts()
            fig = px.pie(
                values=action_counts.values,
                names=action_counts.index,
                title="Message Type Distribution"
            )
            st.plotly_chart(fig, use_container_width=True, key="deepdive_action_pie")
        
        with col2:
            agent_counts = df_messages['agent_name'].value_counts()
            fig = px.bar(
                x=agent_counts.index,
                y=agent_counts.values,
                title="Messages by Agent",
                labels={'x': 'Agent', 'y': 'Count'}
            )
            st.plotly_chart(fig, use_container_width=True, key="deepdive_agent_bar")
        
        # Message list with filters
        st.markdown("### Message Explorer")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_agent = st.multiselect(
                "Filter by Agent",
                options=df_messages['agent_name'].unique().tolist(),
                default=df_messages['agent_name'].unique().tolist()
            )
        
        with col2:
            filter_action = st.multiselect(
                "Filter by Action",
                options=df_messages['action_type'].unique().tolist(),
                default=df_messages['action_type'].unique().tolist()
            )
        
        with col3:
            show_content = st.checkbox("Show Full Content", value=False)
        
        # Apply filters
        filtered_df = df_messages[
            (df_messages['agent_name'].isin(filter_agent)) &
            (df_messages['action_type'].isin(filter_action))
        ]
        
        # Display messages
        for idx, msg in filtered_df.iterrows():
            with st.expander(
                f"Step {msg['step']}: [{msg['agent_name']}] {msg['action_type']} - "
                f"{msg['total_tokens']} tokens, ₹{msg['cost_inr']:.4f}"
            ):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Input Tokens", msg['input_tokens'])
                with col2:
                    st.metric("Output Tokens", msg['output_tokens'])
                with col3:
                    st.metric("Duration", f"{msg['execution_time']:.2f}s")
                
                if msg['system_prompt_tokens'] > 0:
                    st.info(f"System Prompt: {msg['system_prompt_tokens']} tokens (₹{msg['system_prompt_cost_inr']:.4f})")
                
                if msg['tool_name']:
                    st.warning(f"Tool: {msg['tool_name']}")
                
                if msg['handoff_to']:
                    st.success(f"Handoff to: {msg['handoff_to']}")
                
                if show_content and msg['content']:
                    st.markdown("**Content:**")
                    st.text(msg['content'][:500] + ('...' if len(msg['content']) > 500 else ''))
    
    else:
        st.info("No detailed message log available")
    
    # Conversation flow text
    st.markdown("---")
    st.subheader("Full Conversation Flow")
    
    conv_flow = primary_data.get('conversation_flow_txt')
    if conv_flow:
        with st.expander("View Full Conversation Flow", expanded=False):
            st.text(conv_flow)


# ============================================================================
# TAB 5: TOOL ANALYTICS
# ============================================================================

with tab5:
    st.header("Tool Usage Analytics")
    
    primary_data = session_data_list[0]
    tool_analytics = primary_data.get('tool_analytics')
    
    if tool_analytics is not None and not tool_analytics.empty:
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Unique Tools", len(tool_analytics))
        
        with col2:
            st.metric("Total Calls", tool_analytics['call_count'].sum())
        
        with col3:
            st.metric("Total Cost", f"₹{tool_analytics['total_cost_inr'].sum():.4f}")
        
        with col4:
            avg_success = (tool_analytics['success_count'].sum() / tool_analytics['call_count'].sum()) * 100
            st.metric("Avg Success Rate", f"{avg_success:.1f}%")
        
        st.markdown("---")
        
        # Tool usage chart
        fig = create_tool_usage_chart(primary_data)
        if fig:
            st.plotly_chart(fig, use_container_width=True, key="tools_usage_bar")
        
        # Performance metrics
        st.markdown("### Tool Performance Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Avg tokens per call
            fig = px.bar(
                tool_analytics,
                x='tool_name',
                y='avg_tokens_per_call',
                title="Average Tokens per Call",
                color='agent_name'
            )
            st.plotly_chart(fig, use_container_width=True, key="tools_avg_tokens")
        
        with col2:
            # Avg time per call
            fig = px.bar(
                tool_analytics,
                x='tool_name',
                y='avg_time_per_call',
                title="Average Execution Time per Call (seconds)",
                color='agent_name'
            )
            st.plotly_chart(fig, use_container_width=True, key="tools_avg_time")
        
        # Detailed table
        st.markdown("### Detailed Tool Statistics")
        
        display_df = tool_analytics.copy()
        display_df['total_cost_inr'] = display_df['total_cost_inr'].apply(lambda x: f"₹{x:.4f}")
        display_df['success_rate'] = display_df['success_rate'].apply(lambda x: f"{x:.1f}%")
        display_df['avg_tokens_per_call'] = display_df['avg_tokens_per_call'].apply(lambda x: f"{x:.1f}")
        display_df['avg_time_per_call'] = display_df['avg_time_per_call'].apply(lambda x: f"{x:.2f}s")
        
        st.dataframe(display_df, use_container_width=True)
    
    else:
        st.info("No tool analytics data available")


# ============================================================================
# TAB 6: COST ANALYSIS
# ============================================================================

with tab6:
    st.header("Cost Analysis & Budget Tracking")
    
    if len(session_data_list) > 1:
        st.subheader("Multi-Session Cost Comparison")
        
        # Prepare comparison data
        comparison_data = []
        for data in session_data_list:
            summary = data.get('session_summary')
            if summary is not None and not summary.empty:
                row = summary.iloc[0]
                comparison_data.append({
                    'Session': data['session_name'],
                    'Total Cost': row['total_cost_inr'],
                    'System Prompts': row['system_prompt_cost_inr'],
                    'Conversation': row['conversation_cost_inr'],
                    'Total Tokens': row['total_tokens'],
                    'Duration': row['total_execution_time']
                })
        
        df_comparison = pd.DataFrame(comparison_data)
        
        # Cost comparison chart
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='System Prompts',
            x=df_comparison['Session'],
            y=df_comparison['System Prompts'],
            marker_color='#667eea'
        ))
        
        fig.add_trace(go.Bar(
            name='Conversation',
            x=df_comparison['Session'],
            y=df_comparison['Conversation'],
            marker_color='#764ba2'
        ))
        
        fig.update_layout(
            title="Cost Comparison Across Sessions",
            xaxis_title="Session",
            yaxis_title="Cost (INR)",
            barmode='stack',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True, key="cost_comparison_multi")
        
        # Comparison table
        st.dataframe(df_comparison, use_container_width=True)
    
    else:
        primary_data = session_data_list[0]
        summary = primary_data.get('session_summary')
        
        if summary is not None and not summary.empty:
            row = summary.iloc[0]
            
            # Cost breakdown
            st.subheader("Cost Breakdown")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Pie chart
                fig = create_cost_breakdown_chart(primary_data)
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="cost_breakdown_pie")
            
            with col2:
                # Cost metrics
                st.markdown("### Cost Metrics")
                st.metric("Total Cost", f"₹{row['total_cost_inr']:.2f}")
                st.metric("System Prompts Cost", f"₹{row['system_prompt_cost_inr']:.2f}")
                st.metric("Conversation Cost", f"₹{row['conversation_cost_inr']:.2f}")
                
                # Cost per token
                cost_per_token = row['total_cost_inr'] / row['total_tokens'] if row['total_tokens'] > 0 else 0
                st.metric("Cost per 1K Tokens", f"₹{cost_per_token * 1000:.4f}")
            
            # Agent cost breakdown
            st.markdown("### Cost by Agent")
            agent_perf = primary_data.get('agent_performance')
            
            if agent_perf is not None and not agent_perf.empty:
                fig = px.treemap(
                    agent_perf,
                    path=['agent_name'],
                    values='total_cost_inr',
                    title="Agent Cost Distribution (Treemap)",
                    color='total_cost_inr',
                    color_continuous_scale='Purples'
                )
                st.plotly_chart(fig, use_container_width=True, key="cost_treemap_agents")
            
            # Budget tracker
            st.markdown("---")
            st.subheader("Budget Tracker")
            
            budget = st.number_input("Set Budget (INR)", min_value=0.0, value=10.0, step=0.1)
            
            spent = row['total_cost_inr']
            remaining = budget - spent
            pct_used = (spent / budget * 100) if budget > 0 else 0
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Budget", f"₹{budget:.2f}")
            
            with col2:
                st.metric("Spent", f"₹{spent:.2f}", delta=f"{pct_used:.1f}%")
            
            with col3:
                st.metric("Remaining", f"₹{remaining:.2f}")
            
            # Progress bar
            st.progress(min(pct_used / 100, 1.0))
            
            if pct_used > 100:
                st.error(f"⚠️ Budget exceeded by ₹{abs(remaining):.2f}!")
            elif pct_used > 80:
                st.warning(f"⚠️ {100 - pct_used:.1f}% budget remaining")
            else:
                st.success(f"✅ {remaining / budget * 100:.1f}% budget remaining")


# ============================================================================
# TAB 7: RAW DATA EXPLORER
# ============================================================================

with tab7:
    st.header("Raw Data Explorer")
    
    primary_data = session_data_list[0]
    
    # File selector
    available_data = [
        'session_summary',
        'agent_performance',
        'tool_analytics',
        'routing_data',
        'system_prompts_tracking',
        'system_prompts_summary'
    ]
    
    selected_file = st.selectbox(
        "Select data file to view",
        options=available_data
    )
    
    # Display selected data
    data = primary_data.get(selected_file)
    
    if data is not None and not data.empty:
        st.subheader(f"{selected_file.replace('_', ' ').title()}")
        
        # Data preview
        st.dataframe(data, use_container_width=True)
        
        # Download button
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name=f"{selected_file}.csv",
            mime="text/csv"
        )
        
        # Basic statistics
        st.markdown("### Data Statistics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Rows", len(data))
        
        with col2:
            st.metric("Columns", len(data.columns))
        
        with col3:
            st.metric("Memory Usage", f"{data.memory_usage(deep=True).sum() / 1024:.1f} KB")
        
        # Column info
        if st.checkbox("Show Column Info"):
            st.markdown("### Column Details")
            col_info = pd.DataFrame({
                'Column': data.columns,
                'Type': data.dtypes.values,
                'Non-Null': data.count().values,
                'Null': data.isnull().sum().values
            })
            st.dataframe(col_info, use_container_width=True)
    
    else:
        st.info(f"No data available for {selected_file}")
    
    # Text files
    st.markdown("---")
    st.subheader("Text Files")
    
    text_file = st.selectbox(
        "Select text file",
        options=['conversation_flow_txt', 'system_prompts_full_txt']
    )
    
    text_data = primary_data.get(text_file)
    if text_data:
        st.text_area(
            f"{text_file.replace('_', ' ').title()}",
            value=text_data,
            height=400
        )
        
        # Download button
        st.download_button(
            label="📥 Download Text File",
            data=text_data.encode('utf-8'),
            file_name=f"{text_file}.txt",
            mime="text/plain"
        )
    else:
        st.info(f"No data available for {text_file}")


# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Token Tracking Dashboard v1.0 | Built for Multi-Agent Analytics</p>
    <p>📊 Analyzing: {}</p>
</div>
""".format(', '.join([d['session_name'] for d in session_data_list])), unsafe_allow_html=True)