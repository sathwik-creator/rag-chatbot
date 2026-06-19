from langchain_groq import ChatGroq

from src.vector_db import load_vector_store


def get_rag_response(question, api_key):

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

Context:
{context}

Question:
{question}

Answer:
"""

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    response = llm.invoke(prompt)

    return response.content, docs