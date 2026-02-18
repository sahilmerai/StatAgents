import pandas as pd
import networkx as nx
from pyvis.network import Network
import os

# GraphRAG output path
GRAPHRAG_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\ECO Brain\output"

print("📊 Loading GraphRAG data...")

# Load data
entities = pd.read_parquet(os.path.join(GRAPHRAG_PATH, "entities.parquet"))
relationships = pd.read_parquet(os.path.join(GRAPHRAG_PATH, "relationships.parquet"))

print("Entities columns:", entities.columns.tolist())
print("Relationships columns:", relationships.columns.tolist())

# Find entity name column
entity_col = 'title' if 'title' in entities.columns else 'name' if 'name' in entities.columns else 'id'
print(f"\n✅ Using entity column: '{entity_col}'")

# Create graph
G = nx.Graph()

# Add nodes - CLEAN special characters
for idx, row in entities.head(150).iterrows():
    node_name = str(row[entity_col])
    node_type = row.get('type', 'concept')
    description = str(row.get('description', ''))[:300]
    
    # Remove problematic Unicode characters
    description = description.encode('ascii', 'ignore').decode('ascii')
    node_name_clean = node_name.encode('ascii', 'ignore').decode('ascii')
    
    G.add_node(
        node_name,
        title=f"<b>{node_name_clean}</b><br><br>{description}",
        label=node_name_clean,
        group=node_type
    )

# Add edges
edge_count = 0
for idx, row in relationships.head(250).iterrows():
    source = str(row['source'])
    target = str(row['target'])
    if source in G.nodes and target in G.nodes:
        G.add_edge(source, target)
        edge_count += 1

print(f"\n✅ Graph: {G.number_of_nodes()} nodes, {edge_count} edges")

# Create visualization
net = Network(
    height="950px", 
    width="100%", 
    notebook=False,
    bgcolor="#ffffff",
    font_color="black",
    select_menu=True
)

# Smooth physics
net.barnes_hut(
    gravity=-8000,
    central_gravity=0.3,
    spring_length=150,
    spring_strength=0.001,
    damping=0.09,
    overlap=0
)

net.from_nx(G)

# Visual options
net.set_options("""
{
  "nodes": {
    "borderWidth": 2,
    "font": {
      "size": 16,
      "face": "Arial"
    },
    "size": 25,
    "shadow": {
      "enabled": true,
      "size": 10
    }
  },
  "edges": {
    "color": {
      "color": "rgba(200,200,200,0.5)"
    },
    "smooth": true,
    "width": 1
  },
  "physics": {
    "enabled": true,
    "stabilization": {
      "iterations": 200
    }
  }
}
""")

# Save with UTF-8 encoding - FIX FOR UNICODE ERROR
html = net.generate_html()
with open("ECO_knowledge_graph.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\n✅ Saved: DOE_knowledge_graph.html")
print("🌐 Open in browser!")