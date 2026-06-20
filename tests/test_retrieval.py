from src.rag_chain import retrieve_documents


def test_retrieve_documents():
    docs = retrieve_documents("What are Sathwik's skills?")

    assert docs is not None
    assert len(docs) > 0
    assert docs[0].page_content is not None
