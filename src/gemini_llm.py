from langchain_google_genai import ChatGoogleGenerativeAI

def generate(prompt, api_key):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0
    )

    response = llm.invoke(prompt)

    return response.content