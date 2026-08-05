from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

docs = [
    Document(page_content="Hello World")
]

print("Before Chroma")

db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="test_db"
)

print("Success")