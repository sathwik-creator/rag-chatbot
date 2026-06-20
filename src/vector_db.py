import streamlit as st
from langchain_community.vectorstores import FAISS

from src.embeddings import get_embedding_model


def create_vector_store(chunks):
    embeddings = get_embedding_model()

    return FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )


def save_vector_store(vectorstore):
    vectorstore.save_local("vectorstore")


@st.cache_resource
def load_cached_vector_store():
    embeddings = get_embedding_model()

    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True,
    )


def load_vector_store():
    return load_cached_vector_store()
