import json
from config import client, MODEL
from my_tools import TOOLS, TOOL_FUNCTIONS



def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI agent. The college fee information is stored in the local file Day_3/notice.html. Always use the read_webpage tool with Day_3/notice.html to get fee information. Use the calculator tool for calculations. Do not search the internet or guess information."
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

                try:
                    arguments = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError:
                    arguments = {}

                print("Tool:", tool_name)
                print("Arguments:", arguments)

                if tool_name in TOOL_FUNCTIONS:
                    try:
                        result = TOOL_FUNCTIONS[tool_name](**arguments)
                    except Exception as e:
                        result = f"Tool error: {e}"
                else:
                    result = "Unknown tool"

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