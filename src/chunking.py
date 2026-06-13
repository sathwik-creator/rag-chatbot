from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    """
    Split LangChain documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    return chunks