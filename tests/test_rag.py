from src.rag_chain import get_rag_response


def test_rag_response():
    answer, docs = get_rag_response(
        "What are Sathwik's skills?",
        "Ollama",
    )

    assert answer is not None
    assert len(answer) > 0
    assert docs is not None
    assert len(docs) > 0
