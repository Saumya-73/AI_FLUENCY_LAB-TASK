import json

from config import client, MODEL
from my_tool import TOOL, calculator


questions = [
    "What is the fee for AI202?",
    "What is 12000 + 18000?",
    "What is the difference between 15000 and 12000?"
]


for question in questions:
    print("\n================================")
    print("Question:", question)
    print("================================")

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant. "
                "The calculator tool is available for arithmetic calculations. "
                "Use the calculator when a calculation is needed."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=[TOOL],
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message

    if message.tool_calls:
        messages.append(message)

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print("Tool call:")
            print("Tool:", tool_name)
            print("Arguments:", arguments)

            if tool_name == "calculator":
                result = calculator(arguments["expression"])
            else:
                result = "Unknown tool"

            print("Tool result:", result)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            )

        final_response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0
        )

        print("Final answer:")
        print(final_response.choices[0].message.content)

    else:
        print("No tool call.")
        print("Final answer:")
        print(message.content)