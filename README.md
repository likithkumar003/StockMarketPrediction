# 🧠 AI-Powered RAG Assistant

An intelligent Streamlit-based assistant that analyzes multiple PDF documents and answers user queries using a **Retrieval-Augmented Generation (RAG)** pipeline. If the answer isn't found in the provided documents, it **falls back to Gemini (Google GenAI)** for accurate general legal responses.

---

## 🚀 Demo

📌 Ask questions directly from uploaded PDFs  
📌 Automatically switches to Gemini if answers are not in the documents  
📌 Supports multi-PDF uploads and advanced chunk-based vector retrieval  

---

## 📂 Features

- ✅ Multi-PDF document ingestion & parsing (via `PyPDF2`)
- ✅ Semantic chunking using `LangChain`'s text splitter
- ✅ FAISS-based vector similarity search
- ✅ Prompt-driven Q&A using `LangChain` + `Gemini`
- ✅ Fallback to Gemini for general knowledge queries
- ✅ Clean and responsive UI with `Streamlit`

---

## 🛠️ Tech Stack

| Component         | Technology               |
|------------------|--------------------------|
| Frontend/UI      | Streamlit                |
| Backend Logic    | Python                   |
| LLM Integration  | Google Gemini (via LangChain) |
| Embeddings       | Google Generative AI Embeddings |
| Vector Store     | FAISS                    |
| Document Parsing | PyPDF2                   |

---

## 📦 Installation
### Clone
    git clone https://github.com/your-username/legal-assistant-rag
### direct to the file
    cd legal-assistant-rag
### Env setup
    python -m venv venv
    source venv/bin/activate # On Mac  
    venv\Scripts\activate # On Windows
### Install Dependencies
    pip install -r requirements.txt
### Create a .env file and add your Google API Key:
    GOOGLE_API_KEY=your_google_api_key_here
### 🧪 Run the App
    streamlit run models.py

