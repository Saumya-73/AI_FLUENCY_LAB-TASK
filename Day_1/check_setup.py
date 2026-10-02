from config import client, MODEL, PROVIDER

print("Provider:", PROVIDER)
print("Model:", MODEL)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Say hello in one short sentence."}
    ]
)

print("LLM response:", response.choices[0].message.content)