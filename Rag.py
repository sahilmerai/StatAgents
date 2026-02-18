# create_faiss_index.py
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os
import time

load_dotenv()

# Paths
INPUT_FILE = r"F:\Project work\Cafe Restaurant Analysis\Agents\HOD Brain\workflow_knowledge\workflow_knowledge.md"
OUTPUT_DIR = r"F:\Project work\Cafe Restaurant Analysis\Agents\HOD Brain\workflow_knowledge"

print("📚 Loading DOE Book...")

# Load document
loader = TextLoader(INPUT_FILE, encoding='utf-8')
documents = loader.load()

print(f"✅ Loaded document: {len(documents[0].page_content)} characters")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=150,
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = text_splitter.split_documents(documents)
print(f"✅ Created {len(chunks)} chunks")

# Create embeddings
embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

print("\n🔄 Creating FAISS index (processing in batches to avoid rate limits)...")

# Process in batches to avoid rate limits
BATCH_SIZE = 10  # Process 10 chunks at a time
vectorstore = None

for i in range(0, len(chunks), BATCH_SIZE):
    batch = chunks[i:i+BATCH_SIZE]
    batch_num = (i // BATCH_SIZE) + 1
    total_batches = (len(chunks) + BATCH_SIZE - 1) // BATCH_SIZE
    
    print(f"Processing batch {batch_num}/{total_batches} ({len(batch)} chunks)...")
    
    try:
        if vectorstore is None:
            # Create initial vectorstore
            vectorstore = FAISS.from_documents(batch, embeddings)
        else:
            # Add to existing vectorstore
            vectorstore.add_documents(batch)
        
        # Wait between batches to avoid rate limit
        if i + BATCH_SIZE < len(chunks):
            print("   Waiting 3 seconds...")
            time.sleep(3)
            
    except Exception as e:
        print(f"❌ Error on batch {batch_num}: {e}")
        print("   Waiting 60 seconds and retrying...")
        time.sleep(60)
        
        # Retry the batch
        if vectorstore is None:
            vectorstore = FAISS.from_documents(batch, embeddings)
        else:
            vectorstore.add_documents(batch)

# Save
os.makedirs(OUTPUT_DIR, exist_ok=True)
vectorstore.save_local(OUTPUT_DIR)

print(f"\n✅ FAISS index saved to: {OUTPUT_DIR}")
print(f"📊 Total chunks indexed: {len(chunks)}")