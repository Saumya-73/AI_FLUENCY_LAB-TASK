import json
from config import client, MODEL
from my_tools import TOOLS, TOOL_FUNCTIONS


def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI agent. "
                "Use the available tools when needed. "
                "Think, choose a tool, observe the result, and continue until you can answer."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(6):
        print(f"\n--- Step {step + 1} ---")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                print("Tool:", tool_name)
                print("Arguments:", arguments)

                if tool_name not in TOOL_FUNCTIONS:
                    result = "Unknown tool"
                else:
                    try:
                        result = TOOL_FUNCTIONS[tool_name](**arguments)
                    except Exception as e:
                        result = f"Tool error: {e}"

                print("Observation:", result)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

        else:
            print("\nFinal answer:")
            print(message.content)
            return


    print("\nAgent stopped: maximum steps reached.")


questions = [
    "What is the fee for AI202?",
    "Calculate the total fee for CS101 and AI202 after a 10% scholarship.",
    "What is the difference between DS303 and CS101 fees?"
]


for question in questions:
    print("\n================================")
    print("Question:", question)
    print("================================")
    run_agent(question)