import os

import streamlit as st

from src.document_parser import parse_pdf
from src.qa_pipeline import answer_question
from src.section_store import save_sections

st.set_page_config(page_title="Document QA", page_icon="📄", layout="wide")

st.title("📄 Document Question Answering")

st.markdown("""
Upload a PDF and ask questions about its content.

### Available Models
- 🚀 Groq (Cloud)
- 🖥️ Ollama (Local)
""")

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("⚙️ Settings")

llm_choice = st.sidebar.radio("Choose LLM", ["Groq", "Ollama"])

api_key = ""

if llm_choice == "Groq":
    api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

    if api_key:
        st.sidebar.success("✅ Groq API Key Loaded")
    else:
        st.sidebar.warning("⚠️ Enter Groq API Key")

else:
    st.sidebar.success("✅ Using Ollama (Local Mistral)")

# ==========================
# PDF UPLOAD
# ==========================

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join("uploads", uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("📄 Processing document..."):
        sections = parse_pdf(pdf_path)

        save_sections(sections)

    st.success(
        f"✅ Document processed successfully ({len(sections)} sections extracted)"
    )

# ==========================
# QUESTION SECTION
# ==========================

st.divider()

question = st.text_input("Ask a question about the document")

if st.button("🚀 Get Answer"):
    if uploaded_file is None:
        st.warning("Please upload a PDF first.")

    elif not question:
        st.warning("Please enter a question.")

    elif llm_choice == "Groq" and not api_key:
        st.error("Please enter a Groq API Key.")

    else:
        try:
            with st.spinner(f"Generating answer using {llm_choice}..."):
                answer = answer_question(question, llm_choice, api_key)

            st.subheader("📌 Answer")

            st.write(answer)

        except Exception as e:
            st.error(f"Error: {str(e)}")

# ==========================
# FOOTER
# ==========================

st.divider()

st.caption("Powered by PyMuPDF4LLM + Groq/Ollama")
