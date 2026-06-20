import ollama


def generate(prompt: str) -> str:
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return str(response["message"]["content"])
