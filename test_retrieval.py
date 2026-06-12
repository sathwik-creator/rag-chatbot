from src.rag_chain import retrieve_documents

query = "What skills does Sathwik have?"

results = retrieve_documents(query)

print(f"Retrieved Chunks: {len(results)}")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Chunk {i} ---")
    print(doc.page_content[:500])