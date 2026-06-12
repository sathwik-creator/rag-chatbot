from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

from src.vector_db import load_vector_store

load_dotenv()


def get_rag_response(question):

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

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )

    response = llm.invoke(prompt)

    return response.content, docs