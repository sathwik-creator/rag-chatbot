from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model


def create_vector_store(chunks):
    embeddings = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore


def save_vector_store(vectorstore):
    vectorstore.save_local("vectorstore")


def load_vector_store():
    embeddings = get_embedding_model()

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore