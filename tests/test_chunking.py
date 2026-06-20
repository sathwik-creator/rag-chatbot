from src.chunking import chunk_documents
from src.pdf_loader import load_pdf


def test_chunk_documents():
    documents = load_pdf("uploads/Dubakunta_Sathwik_Resume.pdf")

    chunks = chunk_documents(documents)

    assert len(documents) > 0
    assert len(chunks) > 0
    assert chunks[0].page_content is not None
    assert len(chunks[0].page_content) > 0
