from langchain_groq import ChatGroq


def generate(prompt, api_key):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=512
    )

    response = llm.invoke(prompt)

    return response.content