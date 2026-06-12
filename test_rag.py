from src.rag_chain import get_rag_response

question = "What are Sathwik's skills?"

answer, docs = get_rag_response(question)

print("=" * 50)
print("ANSWER")
print("=" * 50)

print(answer)

print("\n")
print("=" * 50)
print("SOURCES")
print("=" * 50)

for i, doc in enumerate(docs, start=1):

    print(f"\n--- Source {i} ---")
    print(doc.page_content[:500])