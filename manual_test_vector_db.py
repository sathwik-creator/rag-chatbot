from src.chunking import chunk_documents
from src.pdf_loader import load_pdf
from src.vector_db import create_vector_store, load_vector_store, save_vector_store

print("=" * 50)
print("VECTOR DATABASE TEST")
print("=" * 50)

documents = load_pdf("uploads/sample.pdf")

chunks = chunk_documents(documents)

print(f"Chunks: {len(chunks)}")

vectorstore = create_vector_store(chunks)

save_vector_store(vectorstore)

print("\nFAISS Vector Store Created Successfully")

loaded_db = load_vector_store()

results = loaded_db.similarity_search("What skills does Sathwik have?", k=3)

print(f"\nRetrieved Chunks: {len(results)}")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Chunk {i} ---")
    print(doc.page_content[:500])
