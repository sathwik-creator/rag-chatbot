from src.vector_db import load_vector_store


def get_rag_response(question, llm_type, api_key=None):

    vectorstore = load_vector_store()

    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

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

        from src.groq_llm import generate

        answer = generate(
            prompt,
            api_key
        )

    else:

        from src.ollama_llm import generate

        answer = generate(
            prompt
        )

    return answer, docs