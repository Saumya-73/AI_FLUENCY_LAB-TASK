import json
import os

from openai import OpenAI
from dotenv import load_dotenv

from tools import TOOLS, TOOL_FUNCTIONS
from validate import validate_arguments


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-120b"

MAX_STEPS = 6
MAX_TOKENS = 1000


def handle_tool_call(tool_call):
    tool_name = tool_call.function.name
    raw_arguments = tool_call.function.arguments

    # Step 1: Parse JSON
    try:
        arguments = json.loads(raw_arguments)
    except json.JSONDecodeError as e:
        return f"Argument error: invalid JSON: {e}"

    # Step 2: Check tool name
    if tool_name not in TOOL_FUNCTIONS:
        available = ", ".join(TOOL_FUNCTIONS.keys())
        return f"Unknown tool: {tool_name}. Available tools: {available}."

    # Step 3: Validate arguments
    error = validate_arguments(tool_name, arguments)

    if error:
        return f"Argument error: {error}"

    # Step 4: Execute the tool
    try:
        result = TOOL_FUNCTIONS[tool_name](**arguments)
        return str(result)
    except Exception as e:
        return f"Tool error: {e}"


def agent(question):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful college canteen assistant. "
                "Use tools when needed. "
                "Do not invent food prices."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    max_tokens = MAX_TOKENS
    previous_calls = []

    for step in range(1, MAX_STEPS + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            max_tokens=max_tokens
        )

        message = response.choices[0].message
        finish_reason = response.choices[0].finish_reason

        print(f" step {step}: finish_reason={finish_reason}")

        # Retry if the response was truncated
        if finish_reason == "length":
            if max_tokens < 2000:
                max_tokens = min(max_tokens * 2, 2000)
                print(f"  Response truncated. Retrying with max_tokens={max_tokens}")
                continue

            return "The model response was truncated."

        # No tool call
        if not message.tool_calls:
            return message.content or "No final answer."

        # Detect repeated identical calls
        current_calls = []

        for tool_call in message.tool_calls:
            current_calls.append(
                (
                    tool_call.function.name,
                    tool_call.function.arguments
                )
            )

        if current_calls in previous_calls:
            return "Stopped because the model repeated the same tool call."

        previous_calls.append(current_calls)

        print(f"  {len(message.tool_calls)} tool call(s)")

        # Add assistant message containing tool calls
        messages.append(message)

        # Execute every tool call
        for tool_call in message.tool_calls:

            result = handle_tool_call(tool_call)

            print(
                f"  {tool_call.function.name}"
                f"({tool_call.function.arguments}) -> {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )

    return "Stopped because maximum steps were reached."


if __name__ == "__main__":

    questions = [
        "What is the price of dosa?",
        "What is the price of dosa for lunch and the price of fried rice for dinner? Please look up both prices using the available tools.",
        "What is the price of dosa for brunch?",
        "Write a one-line welcome message for new canteen students."
    ]

    print(
        f"=== CANTEEN ROBUST AGENT | "
        f"provider: groq | model: {MODEL} ==="
    )

    for question in questions:
        print("\nQ:", question)

        try:
            answer = agent(question)
            print("A:", answer)
        except Exception as e:
            print("Agent error:", e)