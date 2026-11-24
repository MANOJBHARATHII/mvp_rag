<div align="center">

# MVP RAG

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=30&pause=1000&color=2563EB&center=true&vCenter=true&width=720&lines=Retrieval-Augmented+Generation;PDF+Knowledge+Chatbot;LangChain+%7C+ChromaDB+%7C+Groq" />

**A local PDF question-answering system powered by Gemini embeddings and Groq LLM.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-FF6F61?style=for-the-badge)](https://www.trychroma.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama%203.3-F55036?style=for-the-badge)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge)](LICENSE)

</div>

## Overview

MVP RAG reads PDF documents, converts their content into searchable vector embeddings, and answers user questions using only the most relevant document sections. It combines LangChain, Gemini embeddings, ChromaDB, and the Groq-hosted Llama 3.3 model.

## How It Works

### 1. Ingestion

`ingect.py` loads a PDF using `PyPDFLoader`, splits the document into manageable chunks with `RecursiveCharacterTextSplitter`, and generates embeddings using Google's `text-embedding-004` model.

### 2. Storage

The generated vectors and corresponding text chunks are stored persistently in a local ChromaDB collection.

### 3. Retrieval

When a question is entered in the terminal, its embedding is generated with the same Gemini embedding model. ChromaDB retrieves the four most relevant chunks.

### 4. Generation

LangChain sends the retrieved context and user question to Groq's Llama 3.3 70B Versatile model. The model answers from the PDF context and reduces the risk of hallucination.

## Architecture

```text
PDF Document
     |
     v
PyPDFLoader
     |
     v
RecursiveCharacterTextSplitter
     |
     v
Gemini text-embedding-004
     |
     v
Persistent ChromaDB
     |
     v
User Question -> Gemini Embedding -> Similarity Search
                                      |
                                      v
                         Top 4 Relevant Chunks
                                      |
                                      v
                         LangChain -> Groq LLM
                                      |
                                      v
                               Terminal Answer
