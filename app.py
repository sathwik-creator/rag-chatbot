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

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")

    documents = load_pdf(file_path)

    chunks = chunk_documents(documents)

    vectorstore = create_vector_store(chunks)

    save_vector_store(vectorstore)

    st.success("Vector Database Created Successfully")

    st.write(f"Pages Loaded: {len(documents)}")
    st.write(f"Chunks Created: {len(chunks)}")

    question = st.text_input(
        "Ask a question about the PDF"
    )

    if question:

        with st.spinner("Generating answer..."):

            answer, docs = get_rag_response(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for i, doc in enumerate(docs, start=1):
            with st.expander(f"Source {i}"):
                st.write(doc.page_content)