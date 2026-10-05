import json
import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-120b"


QUESTION = (
    "Extract the canteen request from this sentence: "
    "'I want the price of dosa for lunch.'"
)


def show_result(title, raw):
    print(f"\n--- {title} ---")
    print("raw :", raw)

    try:
        parsed = json.loads(raw)
        print("parsed:", parsed)
    except json.JSONDecodeError as e:
        print(f"not valid JSON ({type(e).__name__}: {e})")


# 1. Free text
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": QUESTION
        }
    ],
    max_tokens=200
)

raw = response.choices[0].message.content
show_result("1. no constraint (free text)", raw)


# 2. JSON mode
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": (
                QUESTION
                + " Return only valid JSON with keys "
                  "food_name and meal_type."
            )
        }
    ],
    response_format={"type": "json_object"},
    max_tokens=200
)

raw = response.choices[0].message.content
show_result("2. JSON mode", raw)


# 3. Structured schema mode
schema = {
    "type": "object",
    "properties": {
        "food_name": {
            "type": "string",
            "enum": ["idly", "dosa", "fried_rice"]
        },
        "meal_type": {
            "type": "string",
            "enum": ["breakfast", "lunch", "dinner"]
        }
    },
    "required": ["food_name", "meal_type"],
    "additionalProperties": False
}


try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "canteen_request",
                "strict": True,
                "schema": schema
            }
        },
        max_tokens=200
    )

    raw = response.choices[0].message.content
    show_result("3. schema mode", raw)

except Exception as e:
    print("\n--- 3. schema mode ---")
    print("Schema mode error:", e)