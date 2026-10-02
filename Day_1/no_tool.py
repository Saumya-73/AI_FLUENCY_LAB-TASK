from config import client, MODEL, banner

banner("WITHOUT TOOL")

questions = [
    "What is a programming language?",
    "What is the purpose of a college fee?",
    "The fees are 12000, 18000 and 15000. What is the total?"
]

for question in questions:
    print("\nQuestion:", question)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content

    print("LLM Answer:", answer)