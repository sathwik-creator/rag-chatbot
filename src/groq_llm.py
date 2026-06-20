from langchain_groq import ChatGroq
from pydantic import SecretStr


def generate(
    prompt: str,
    api_key: str | None = None,
) -> str:
    secret_api_key = SecretStr(api_key) if api_key else None

    llm = ChatGroq(
        api_key=secret_api_key,
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=512,
    )

    response = llm.invoke(prompt)

    return str(response.content)
