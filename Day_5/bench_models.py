import time

from Day5_config import client, PROVIDER

MODELS = [
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b"
]

PROMPTS = [
    "Reply with exactly: OK",
    "In two sentences, what is an AI agent?",
    "A course costs Rs. 18,000 with a 15% scholarship. What is payable? Show the steps."
]


def run(model, prompt):
    start = time.time()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    elapsed = time.time() - start
    answer = response.choices[0].message.content

    return elapsed, answer


if __name__ == "__main__":
    print("DAY 5 - MODEL COMPARISON")
    print("========================")
    print("Provider:", PROVIDER)

    for model in MODELS:
        print("\n" + "=" * 60)
        print("MODEL:", model)
        print("=" * 60)

        for prompt in PROMPTS:
            elapsed, answer = run(model, prompt)

            print("\nPrompt:", prompt)
            print(f"Time: {elapsed:.2f} seconds")
            print("Answer:", answer)