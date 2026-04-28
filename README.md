# knowledge_based_RAG_Agent

## 🍽️ Restaurant Chatbot

A lightweight, offline‑ready chatbot that answers customer questions about restaurant menus, hours, location, and services. The bot uses semantic search to retrieve the most relevant piece of information from your restaurant data.

## ✨ Features

- **Local & Free** – Runs entirely on your machine using open‑source models (no API keys or cloud costs).
- **Semantic Search** – Understands natural language questions, not just keywords.
- **Multi‑format Document Support** – Handles `.txt`, `.pdf`, `.docx`, and more via `document_loader.py`.
- **Fast & Lightweight** – Uses a small sentence‑transformer model (`all-MiniLM-L6-v2`) for embeddings.
- **Modular Design** – Easy to update restaurant data or swap components.

## 📁 Project Structure

.
├── chatbot.py # Main chatbot script
├── restaurant_data.txt # Restaurant information (menu, hours, contact, etc.)
├── document_loader.py # (Required) MultiFormatDocumentLoader utility
└── README.md # This file


> **Note**: `document_loader.py` is not shown here but must be present. It should export a `MultiFormatDocumentLoader` class with a `.load()` method.

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone or download** this repository.

2. **Install the required packages**:

```bash
pip install langchain-huggingface langchain-community langchain-text-splitters faiss-cpu sentence-transformers
```

If you plan to use PDF or DOCX files, also install:
```bash
pip install pypdf docx2txt
```

Prepare Your Data
Edit restaurant_data.txt (or add more files) with your own restaurant details.

The loader accepts a list of file paths. Supported formats are automatically detected by MultiFormatDocumentLoader.

### Run the Chatbot

```bash
Run the Chatbot
```

The first run may take ~30 seconds to download the embedding model. Once ready, type your questions – for example:

```text
You: What are your opening hours?
Chatbot: Monday to Friday: 12:00 PM to 11:00 PM, Saturday & Sunday: 1:00 PM to 12:00 AM...

You: Do you have vegetarian options?
Chatbot: Vegetarian menu available. Vegan options on request...
```

### 🛠️ Customization
Parameter in chatbot.py	Effect
chunk_size=150	Smaller chunks = more precise retrieval.
k=1	Number of document chunks returned. Increase to show more context.
model_name="..."	Swap for another HuggingFace embedding model.
data_files list	Add more files (e.g., menu.pdf, events.docx).

### 📋 Example Data (restaurant_data.txt)
The provided file includes:

Opening hours, location, contact

Full menu with prices (appetizers, biryani, karahi, desserts, drinks)

Combo deals, dietary info, payment methods

Loyalty program, safety measures, and more

The chatbot will retrieve exact text snippets based on your question.

### 🧠 How It Works
Load – MultiFormatDocumentLoader reads all supported files.

Split – RecursiveCharacterTextSplitter breaks text into small, overlapping chunks.

Embed – HuggingFaceEmbeddings converts each chunk into a vector.

Store – FAISS indexes the vectors for fast similarity search.

Retrieve – When you ask a question, the bot finds the most similar chunk and returns it as the answer.
