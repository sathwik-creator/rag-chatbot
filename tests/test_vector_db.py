from src.chunking import chunk_documents
from src.pdf_loader import load_pdf
from src.vector_db import create_vector_store


def test_vector_store_creation():
    documents = load_pdf("uploads/Dubakunta_Sathwik_Resume.pdf")

    chunks = chunk_documents(documents)

    vectorstore = create_vector_store(chunks)

    assert vectorstore is not None
