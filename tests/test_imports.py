from src.chunking import chunk_documents
from src.pdf_loader import load_pdf
from src.vector_db import create_vector_store


def test_imports():
    assert chunk_documents is not None
    assert load_pdf is not None
    assert create_vector_store is not None
