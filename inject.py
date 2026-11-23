from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import engine

loader = PyPDFLoader("Medical_book (2).pdf")
text = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
chunks = text_splitter.split_documents(text)
print(f"Loaded {len(text)} PDF pages and created {len(chunks)} chunks.")
engine.add_documents(chunks)