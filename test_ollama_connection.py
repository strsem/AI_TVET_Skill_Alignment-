from ollama import Client


client = Client(
    host="http://localhost:11434"
)

response = client.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ],
    stream=False
)

print(response.message.content)