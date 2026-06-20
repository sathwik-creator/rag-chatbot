from src.vector_db import load_vector_store


def retrieve_documents(
    question: str,
    k: int = 2,
):
    vectorstore = load_vector_store()

    return vectorstore.similarity_search(
        question,
        k=k,
    )


def get_rag_response(
    question: str,
    llm_type: str,
    api_key: str | None = None,
) -> tuple[str, list]:
    docs = retrieve_documents(
        question,
        k=2,
    )

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the context below.

If the answer is not found in the context, say:
'I could not find that information in the document.'

Context:
{context}

Question:
{question}

Answer:
"""

    if llm_type == "Groq":
        from src.groq_llm import generate as groq_generate

        answer = groq_generate(
            prompt,
            api_key,
        )
    else:
        from src.ollama_llm import generate as ollama_generate

        answer = ollama_generate(prompt)

    return answer, docs
