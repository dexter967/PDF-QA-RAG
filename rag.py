import os
import shutil
from dotenv import load_dotenv

from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# ======================================
# Load Environment Variables
# ======================================

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file.")

client = genai.Client(api_key=API_KEY)

DB_PATH = "chroma_db"

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

    # Delete old database
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

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

    print("Creating Chroma DB...")

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

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings,
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    conversation = ""

    for q, a in history:
        conversation += f"User: {q}\nAssistant: {a}\n"

    prompt = f"""
You are an intelligent PDF assistant.

Conversation History:
{conversation}

Context:
{context}

Question:
{question}

Instructions:
- Answer ONLY using the provided context.
- If the answer is not available, reply exactly:
I couldn't find that information in the PDF.
"""

    response = client.models.generate_content(
        model="models/gemini-3.6-flash",
        contents=prompt,
    )

    answer = response.text

    history.append((question, answer))

    return answer, history