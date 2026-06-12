from src.embeddings import get_embedding_model

# Load embedding model
embeddings = get_embedding_model()

# Test sentence
text = "Hello, this is a test for embeddings."

# Generate embedding
vector = embeddings.embed_query(text)

print("=" * 50)
print("EMBEDDING TEST")
print("=" * 50)

print(f"Text: {text}")
print(f"Vector Length: {len(vector)}")

print("\nFirst 10 Values:")
print(vector[:10])