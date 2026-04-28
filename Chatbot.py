from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from document_loader import MultiFormatDocumentLoader
import os

print("Initializing Restaurant Chatbot...")

# Load restaurant data from multiple formats
data_files = [
    "restaurant_data.txt"
]

# Use MultiFormatDocumentLoader
loader = MultiFormatDocumentLoader(file_paths=data_files)
documents = loader.load()

print(f"Loaded {len(documents)} document(s) from {len([f for f in data_files if os.path.exists(f)])} file(s)")

# Split into smaller, more specific chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,  # Smaller chunks for more precise retrieval
    chunk_overlap=20,
    separators=["\n\n", "\n", ":", "-", " ", ""]
)
chunks = text_splitter.split_documents(documents)

# Create embeddings (local, free)
print("Loading embeddings model (first time may take ~30 seconds)...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector store
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})  # Return only the most relevant chunk

print("\n" + "="*60)
print("Restaurant Chatbot is ready! Type 'exit' to quit.")
print("="*60 + "\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("\nChatbot: Thank you for visiting! Have a great day!")
        break
    
    if not user_input.strip():
        continue
    
    # Retrieve the most relevant document
    docs = retriever.invoke(user_input)
    
    # Simple response generation based on retrieved context
    if docs:
        # Get the most relevant chunk
        context = docs[0].page_content.strip()
        
        # Create a simple response
        print(f"\nChatbot: {context}\n")
    else:
        print("\nChatbot: I'm sorry, I don't have information about that. Please ask about our menu, hours, location, or specialties.\n")
