from langchain_groq import ChatGroq


def generate(prompt, api_key):

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    response = llm.invoke(prompt)

    return response.content