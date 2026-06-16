from src.section_store import load_sections


def answer_question(question, llm_type, api_key=None):

    sections = load_sections()

    context = "\n\n".join(sections)

    prompt = f"""
You are a helpful document assistant.

Answer ONLY using the document context below.

If the answer is not present in the document, say:

'I could not find that information in the document.'

Context:
{context}

Question:
{question}

Answer:
"""

    if llm_type == "Groq":

        from src.groq_llm import generate

        return generate(
            prompt,
            api_key
        )

    else:

        from src.ollama_llm import generate

        return generate(
            prompt
        )