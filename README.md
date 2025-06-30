# 🧠 AI-Powered Legal Assistant

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

```bash
git clone https://github.com/your-username/legal-assistant-rag
cd legal-assistant-rag
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
