from src.pdf_loader import load_pdf


def test_pdf_loads():
    documents = load_pdf("uploads/Dubakunta_Sathwik_Resume.pdf")

    assert documents is not None
    assert len(documents) > 0
    assert documents[0].page_content is not None
    assert len(documents[0].page_content) > 0
