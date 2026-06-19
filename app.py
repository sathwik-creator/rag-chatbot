import streamlit as st
import os

from src.pdf_loader import load_pdf
from src.chunking import chunk_documents
from src.vector_db import (
create_vector_store,
save_vector_store
)
from src.rag_chain import get_rag_response

st.set_page_config(
page_title="RAG Chatbot",
page_icon="📄"
)

st.title("📄 RAG Chatbot")

# ==========================

# SIDEBAR SETTINGS

# ==========================

st.sidebar.title("⚙️ LLM Settings")

llm_choice = st.sidebar.radio(
"Choose LLM",
["Groq", "Ollama"]
)

api_key = ""

if llm_choice == "Groq":

api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password"
)

if api_key:
    st.sidebar.success(
        "✅ Groq API Key Loaded"
    )
else:
    st.sidebar.warning(
        "⚠️ Please Enter Groq API Key"
    )
else:

st.sidebar.success(
    "✅ Using Ollama"
)

# ==========================

# PDF UPLOAD

# ==========================

uploaded_file = st.file_uploader(
"Upload PDF",
type=["pdf"]
)

if uploaded_file:
os.makedirs(
    "uploads",
    exist_ok=True
)

file_path = os.path.join(
    "uploads",
    uploaded_file.name
)

with open(file_path, "wb") as f:
    f.write(
        uploaded_file.getbuffer()
    )

st.success(
    f"Uploaded: {uploaded_file.name}"
)

documents = load_pdf(
    file_path
)

chunks = chunk_documents(
    documents
)

vectorstore = create_vector_store(
    chunks
)

save_vector_store(
    vectorstore
)

st.success(
    "Vector Database Created Successfully"
)

st.write(
    f"Pages Loaded: {len(documents)}"
)

st.write(
    f"Chunks Created: {len(chunks)}"
)

question = st.text_input(
    "Ask a question about the PDF"
)

ask_button = st.button(
    "🚀 Get Answer"
)

if ask_button:

    if not question:

        st.warning(
            "Please enter a question."
        )

        st.stop()

    if llm_choice == "Groq" and not api_key:

        st.error(
            "Please enter a Groq API Key."
        )

        st.stop()

    with st.spinner(
        "Generating answer..."
    ):

        answer, docs = get_rag_response(
            question,
            llm_choice,
            api_key
        )

    st.subheader(
        "Answer"
    )

    st.write(
        answer
    )

    st.subheader(
        "Sources"
    )

    for i, doc in enumerate(
        docs,
        start=1
    ):

        with st.expander(
            f"Source {i}"
        ):

            st.write(
                doc.page_content
            )
