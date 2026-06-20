import os

import streamlit as st

from src.chunking import chunk_documents
from src.pdf_loader import load_pdf
from src.rag_chain import get_rag_response
from src.vector_db import create_vector_store, save_vector_store

st.set_page_config(page_title="RAG Chatbot", page_icon="📄", layout="wide")

st.title("📄 RAG Chatbot")
st.markdown("Ask questions from your PDF using Groq or Ollama")

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("⚙️ Settings")

llm_choice = st.sidebar.radio("Choose LLM", ["Groq", "Ollama"])

api_key = ""

if llm_choice == "Groq":
    api_key = st.sidebar.text_input("Groq API Key", type="password")

    if api_key:
        st.sidebar.success("✅ API Key Loaded")
    else:
        st.sidebar.warning("⚠️ Enter Groq API Key")

else:
    st.sidebar.success("✅ Using Ollama")

# ==========================
# PDF UPLOAD
# ==========================

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")

    # ==========================
    # CREATE VECTOR STORE ONLY
    # WHEN NEW PDF IS UPLOADED
    # ==========================

    if (
        "vector_ready" not in st.session_state
        or st.session_state.get("current_file") != uploaded_file.name
    ):
        with st.spinner("📄 Loading PDF..."):
            documents = load_pdf(file_path)

        st.success(f"Loaded {len(documents)} pages")

        with st.spinner("✂️ Creating Chunks..."):
            chunks = chunk_documents(documents)

        st.success(f"Created {len(chunks)} chunks")

        with st.spinner("🧠 Creating Embeddings & Vector Store..."):
            vectorstore = create_vector_store(chunks)

            save_vector_store(vectorstore)

        st.session_state.vector_ready = True
        st.session_state.current_file = uploaded_file.name

        st.success("✅ Vector Database Ready")

    # ==========================
    # QUESTION SECTION
    # ==========================

    question = st.text_input("Ask a question about the PDF")

    ask_button = st.button("🚀 Get Answer")

    if ask_button:
        if not question:
            st.warning("Please enter a question.")

            st.stop()

        if llm_choice == "Groq" and not api_key:
            st.error("Please enter a Groq API Key.")

            st.stop()

        with st.spinner("🤖 Generating Answer..."):
            try:
                answer, docs = get_rag_response(question, llm_choice, api_key)

                st.subheader("Answer")

                st.write(answer)

                st.subheader("Sources")

                for i, doc in enumerate(docs, start=1):
                    with st.expander(f"Source {i}"):
                        st.write(doc.page_content)

            except Exception as e:
                st.error(f"Error: {str(e)}")
