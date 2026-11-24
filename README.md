
### How it Works?

**1. Ingestion Phase (`ingect.py`):**
PDF ah `PyPDFLoader` vechu read pannitu, `RecursiveCharacterTextSplitter` vechu chunks ah odakkurom. Aprom antha chunks ah **Gemini Embedding Model (`models/text-embedding-004`)** vechu vectors ah maathi **ChromaDB** la save pannurom.

**2. Retrieval Phase (`app.py` / `main.py`):**
User terminal la question ketta, athayum Gemini Embedding vechu vector ah maathi, ChromaDB la irunthu Top 4 relevant chunks ah edukkrom.

**3. Generation Phase:**
Antha 4 chunks + Question ah **LangChain** vazhiya **Groq LLM** ku anuppurom. Groq mattum antha PDF la irunthu answer pannum. Velila irunthu hallucinations pannaathu.

## 🛠️ Tech Stack

| Component | Technology |
| --- | --- |
| **Orchestration** | LangChain |
| **Vector DB** | ChromaDB (Local, Persistent) |
| **LLM Model** | Groq - Llama-3.3-70B-Versatile |
| **Embedding Model** | Google Gemini - text-embedding-004 |
| **PDF Loader** | PyPDF |
| **Interface** | CLI / Terminal |

## 📁 Project Structure
