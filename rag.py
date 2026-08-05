import os
import shutil
import tempfile
from dotenv import load_dotenv

from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# ======================================
# Load Environment Variables
# ======================================

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found.")

client = genai.Client(api_key=API_KEY)

DB_PATH = os.path.join(tempfile.gettempdir(), "chroma_db")

# ======================================
# Embedding Model
# ======================================

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=API_KEY,
)

# ======================================
# Process PDF
# ======================================

def process_pdf(pdf_path):

    print("\n========== PDF PROCESSING ==========\n")
    # Reset DB
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH, ignore_errors=True)

    os.makedirs(DB_PATH, exist_ok=True)

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    print(f"Pages : {len(pages)}")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
    )

    docs = splitter.split_documents(pages)

    print(f"Chunks : {len(docs)}")

    print("Generating embeddings...")

    # Create Vector DB
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=DB_PATH,
    )

    print("Chroma DB Created.")
    print("PDF Indexed Successfully.\n")

    return "✅ PDF indexed successfully!"

# ======================================
# Ask Question
# ======================================

def ask_pdf(question, history):

    if not os.path.exists(DB_PATH):
        return (
            "Please upload and index a PDF first.",
            history,
        )

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings,
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    # retrieve relevant documents
    try:
        docs = retriever.get_relevant_documents(question)
    except Exception:
        # fallback if method name differs
        docs = retriever.invoke(question)

    if len(docs) == 0:
        answer = "I couldn't find that information in the PDF."
        history.append((question, answer))
        return answer, history

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    conversation = ""

    for q, a in history[-5:]:
        conversation += f"User: {q}\nAssistant: {a}\n"

    prompt = f"""
You are an intelligent PDF Question Answering Assistant.

Use ONLY the information provided inside the context.

Conversation History:
{conversation}

PDF Context:
{context}

User Question:
{question}

Instructions:

1. Answer ONLY from the PDF.
2. If the answer is not available, reply exactly:
I couldn't find that information in the PDF.
3. Keep answers clear and concise.
4. If the user asks for a summary, summarize only the retrieved PDF content.
5. Do not make up facts.
"""

    try:

        response = client.models.generate_content(
            model="models/gemini-3.6-flash",
            contents=prompt,
        )

        answer = response.text.strip()

    except Exception as e:
        answer = f"Error generating response:\n{e}"

    history.append((question, answer))

    return answer, history