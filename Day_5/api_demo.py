
import time

from Day5_config import client, MODEL, PROVIDER

PROMPT = "In three sentences, explain what an AI agent is."


def generate_once():
    start = time.time()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": PROMPT}
        ],
        temperature=0
    )

    elapsed = time.time() - start
    answer = response.choices[0].message.content

    print("\n[API Generation]")
    print(f"Provider: {PROVIDER}")
    print(f"Model: {MODEL}")
    print(f"Time: {elapsed:.2f} seconds")
    print("Answer:")
    print(answer)


def chat_streaming():
    start = time.time()
    first_token_at = None
    pieces = []

    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": PROMPT}
        ],
        temperature=0,
        stream=True
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content

        if content:
            if first_token_at is None:
                first_token_at = time.time() - start

            pieces.append(content)

    total = time.time() - start
    answer = "".join(pieces)

    print("\n[Streaming]")
    
    
    if first_token_at is not None:
        print(f"TTFT: {first_token_at:.2f} seconds")
    else:
        print("TTFT: No token received")

    print(f"Total time: {total:.2f} seconds")
    print("Answer:")
    print(answer)



if __name__ == "__main__":
    print("DAY 5 - CLOUD API DEMONSTRATION")
    print("================================")

    generate_once()
    chat_streaming()