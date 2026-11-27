from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai._common import GoogleGenerativeAIError
from langchain_core.documents import Document
from pypdf import PdfReader
import time

from config import engine

PDF_PATH = "Medical_book (2).pdf"
BATCH_SIZE = 50

reader = PdfReader(PDF_PATH)
text = [
    Document(
        page_content=page.extract_text() or "",
        metadata={"source": PDF_PATH, "page": page_number},
    )
    for page_number, page in enumerate(reader.pages)
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=200,
)
chunks = text_splitter.split_documents(text)
print(f"Loaded {len(text)} PDF pages and created {len(chunks)} chunks.")

indexed_count = engine._collection.count()
if indexed_count < len(chunks):
    for start in range(indexed_count, len(chunks), BATCH_SIZE):
        batch = chunks[start:start + BATCH_SIZE]
        for attempt in range(4):
            try:
                engine.add_documents(batch)
                print(
                    f"Indexed {min(start + len(batch), len(chunks))}"
                    f"/{len(chunks)} chunks"
                )
                break
            except GoogleGenerativeAIError as error:
                if "free_tier_requests" in str(error) and "per day" in str(error):
                    raise RuntimeError(
                        "Gemini embedding quota is exhausted for the day. "
                        "The partial index is preserved; retry ingestion after quota resets."
                    ) from error
                if attempt == 3:
                    raise
                print(f"Gemini indexing failed ({error}); retrying in 65 seconds...")
                time.sleep(65)

        if start + BATCH_SIZE < len(chunks):
            time.sleep(2)
else:
    print(f"Vector store already contains {engine._collection.count()} chunks.")