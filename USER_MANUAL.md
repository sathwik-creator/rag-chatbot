# User Manual

## Introduction

RAG Chatbot is a Retrieval-Augmented Generation application that allows users to upload PDF documents and ask questions based on their contents.

## Features

* PDF Upload
* Intelligent Chunking
* Vector Embeddings
* Semantic Search
* Question Answering
* Groq Integration
* Ollama Integration

## Installation

```bash
uv sync
```

## Running the Application

```bash
streamlit run app.py
```

## How to Use

1. Launch the application.
2. Upload a PDF document.
3. Wait for processing.
4. Enter your question.
5. View the generated answer.

## Troubleshooting

### Vector Store Not Found

Re-upload the PDF and regenerate embeddings.

### API Key Error

Verify GROQ_API_KEY inside the .env file.

### Slow Responses

Check internet connection or local Ollama status.
