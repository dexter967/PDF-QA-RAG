import os
from dotenv import load_dotenv

from google import genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)

DB_PATH = "chroma_db"

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=API_KEY
)


def process_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    docs = splitter.split_documents(pages)

    if os.path.exists(DB_PATH):
        import shutil
        shutil.rmtree(DB_PATH)

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    vectordb.persist()

    return "✅ PDF indexed successfully!"


def ask_pdf(question, history):

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(search_kwargs={"k":4})

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    conversation = ""

    if history:
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

Answer only from the context.
If the answer is not available, reply:
'I couldn't find that information in the PDF.'
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    history.append((question, answer))

    return history, history