import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not groq_api_key:
    raise RuntimeError("GROQ_API_KEY is not set")
if not gemini_api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=groq_api_key,
)

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=gemini_api_key,
)

engine = Chroma(
    collection_name="mvp_rag_collection",
    embedding_function=embedding_model,
    persist_directory="chroma.db",
)