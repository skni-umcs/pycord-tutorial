import openai

def ask_ai(prompt: str) -> str:
    client = openai.OpenAI(
        base_url="https://api.llm7.io/v1",
        api_key="unused"
    )

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "user", "content": f"{prompt}"}
        ]
    )

    return response.choices[0].message.content