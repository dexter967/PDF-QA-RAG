<div align="center">

# 📄🤖 PDF Question Answering Assistant
### *Retrieval-Augmented Generation (RAG) using Google Gemini*

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit"/>
<img src="https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google"/>
<img src="https://img.shields.io/badge/LangChain-RAG-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ChromaDB-VectorDB-purple?style=for-the-badge"/>

---

### 👨‍💻 Developed by

## **Abhijith A Kurup**

**📧 MUID:** `abhijitha-8@mulearn`

---

## 🚀 Live Demo

### 🌐 https://dexter967-pdf-qa-rag-app-gi2aos.streamlit.app/

</div>

---

# 📌 Project Overview

The **PDF Question Answering Assistant** is an AI-powered application built using **Retrieval-Augmented Generation (RAG)**. It enables users to upload PDF documents and ask questions in natural language. Instead of answering from general knowledge, the assistant retrieves relevant information from the uploaded PDF and generates context-aware responses using **Google Gemini**.

The project combines semantic search with Large Language Models to provide fast, accurate, and document-specific answers.

---

# ✨ Key Features

✅ Upload any PDF document

✅ Automatic text extraction

✅ Intelligent document chunking

✅ Semantic search using Gemini Embeddings

✅ ChromaDB vector database

✅ Google Gemini AI responses

✅ Interactive Streamlit interface

✅ Conversation history

✅ Fast document retrieval

✅ Context-aware question answering

---

# 🧠 How It Works

```text
                📄 Upload PDF
                      │
                      ▼
          Extract Text from PDF
                      │
                      ▼
      Split into Smaller Chunks
                      │
                      ▼
 Generate Gemini Embeddings for Each Chunk
                      │
                      ▼
      Store Vectors in ChromaDB
                      │
                      ▼
          User Asks a Question
                      │
                      ▼
      Retrieve Relevant PDF Chunks
                      │
                      ▼
      Google Gemini Generates Answer
                      │
                      ▼
             Display Response
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 🎈 Streamlit | Web Application |
| 🤖 Google Gemini | Large Language Model |
| 🔗 LangChain | RAG Framework |
| 🗂️ ChromaDB | Vector Database |
| 📑 PyPDF | PDF Loader |
| 🔑 Python Dotenv | API Key Management |

---

# 📂 Project Structure

```
PDF-QA-RAG/
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
├── .env
├── chroma_db/
└── uploads/
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/dexter967/PDF-QA-RAG.git

cd PDF-QA-RAG
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure API Key

Create a `.env` file inside the project folder.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 🌟 Live Deployment

### 🚀 Streamlit Application

## https://dexter967-pdf-qa-rag-app-gi2aos.streamlit.app/

---

# 📷 Application Preview

> Add screenshots after deployment.

Suggested screenshots:

- 🏠 Home Page
- 📄 Upload PDF
- 📚 PDF Indexed Successfully
- 💬 Chat Interface
- 🤖 Generated Answer

---

# 📈 Future Improvements

🔹 Support multiple PDFs simultaneously

🔹 Chat memory across sessions

🔹 Source page references

🔹 Highlight answer inside PDF

🔹 Export chat as PDF

🔹 Dark mode

🔹 Better UI animations

🔹 Voice input

🔹 OCR support for scanned PDFs

---

# 🎯 Learning Outcomes

Through this project, I learned:

- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Vector Embeddings
- ✅ ChromaDB
- ✅ LangChain Pipelines
- ✅ Google Gemini API
- ✅ Prompt Engineering
- ✅ Semantic Search
- ✅ Streamlit Deployment
- ✅ Environment Variable Management
- ✅ Git & GitHub Workflow

---

# 📦 Dependencies

- Streamlit
- Google GenAI
- LangChain
- LangChain Community
- LangChain Google GenAI
- LangChain Text Splitters
- LangChain Chroma
- ChromaDB
- PyPDF
- Python Dotenv

---

# 💡 Why RAG?

Traditional AI models answer based on their training knowledge.

RAG enhances this by:

📄 Retrieving relevant information from your document

🧠 Combining retrieved context with an LLM

✅ Producing accurate, document-grounded answers

This reduces hallucinations and improves response quality.

---

# 📜 License

This project is developed for educational and learning purposes.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a Star!

### Thank You ❤️

**Made with ☕, Python, Streamlit & Google Gemini**

---

### 👨‍💻 Author

## **Abhijith A Kurup**

📧 **MUID:** `abhijitha-8@mulearn`

🌐 **Live Demo:** https://dexter967-pdf-qa-rag-app-gi2aos.streamlit.app/

🐙 **GitHub:** https://github.com/dexter967/PDF-QA-RAG

</div>
