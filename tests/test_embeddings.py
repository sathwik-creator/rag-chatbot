from src.embeddings import get_embedding_model


def test_embedding_model():
    model = get_embedding_model()

    embedding = model.embed_query("What are Sathwik's skills?")

    assert model is not None
    assert embedding is not None
    assert len(embedding) > 0
