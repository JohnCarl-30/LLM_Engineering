from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.2"

client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="", flush=True)