from config import client, MODEL


questions = [
    "What is the fee for AI202?",
    "What is 12000 + 18000?",
    "What is the difference between 15000 and 12000?"
]


for question in questions:
    print("\n================================")
    print("Question:", question)
    print("================================")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer the user's question using only your own knowledge."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    print("Answer:")
    print(response.choices[0].message.content)