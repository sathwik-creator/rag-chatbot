# Agents

## PDF Loader Agent

Responsible for loading PDF documents and extracting text.

## Chunking Agent

Splits documents into smaller chunks for efficient retrieval.

## Embedding Agent

Generates vector embeddings using Sentence Transformers.

## Vector Store Agent

Stores embeddings inside the FAISS vector database.

## Retrieval Agent

Retrieves the most relevant chunks based on user queries.

## LLM Agent

Generates final answers using Groq or Ollama.

## RAG Pipeline Agent

Coordinates retrieval and answer generation.