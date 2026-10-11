from tools import TOOL_FUNCTIONS
from validate import validate_arguments


class FakeCall:
    def __init__(self, name, arguments):
        self.function = type(
            "Function",
            (),
            {
                "name": name,
                "arguments": arguments
            }
        )()


def handle_fake_call(call):
    tool_name = call.function.name
    raw_arguments = call.function.arguments

    import json

    # JSON parsing
    try:
        arguments = json.loads(raw_arguments)
    except json.JSONDecodeError as e:
        return f"Argument error: invalid JSON: {e}"

    # Tool lookup
    if tool_name not in TOOL_FUNCTIONS:
        available = ", ".join(TOOL_FUNCTIONS.keys())
        return f"Unknown tool: {tool_name}. Available tools: {available}."

    # Validation
    error = validate_arguments(tool_name, arguments)

    if error:
        return f"Argument error: {error}"

    # Execute
    try:
        result = TOOL_FUNCTIONS[tool_name](**arguments)
        return str(result)
    except Exception as e:
        return f"Tool error: {e}"


FAULTS = [
    (
        "good call",
        FakeCall(
            "get_food_price",
            '{"food_name": "dosa", "meal_type": "lunch"}'
        )
    ),

    (
        "invalid JSON",
        FakeCall(
            "get_food_price",
            '{"food_name": "dosa",'
        )
    ),

    (
        "unknown tool",
        FakeCall(
            "get_food_cost",
            '{"food_name": "dosa", "meal_type": "lunch"}'
        )
    ),

    (
        "missing required",
        FakeCall(
            "get_food_price",
            '{"food_name": "dosa"}'
        )
    ),

    (
        "wrong type",
        FakeCall(
            "get_food_price",
            '{"food_name": 123, "meal_type": "lunch"}'
        )
    ),

    (
        "invalid enum",
        FakeCall(
            "get_food_price",
            '{"food_name": "dosa", "meal_type": "brunch"}'
        )
    ),

    (
        "invented extra argument",
        FakeCall(
            "get_food_price",
            '{"food_name": "dosa", "meal_type": "lunch", "year": 2026}'
        )
    ),

    # Own design fault 1
    (
        "unknown food",
        FakeCall(
            "get_food_price",
            '{"food_name": "pizza", "meal_type": "lunch"}'
        )
    ),

    # Own design fault 2
    (
        "arguments as array",
        FakeCall(
            "get_food_price",
            '["dosa", "lunch"]'
        )
    ),
]


if __name__ == "__main__":
    for name, call in FAULTS:
        result = handle_fake_call(call)
        print(f"{name:25} -> {result}")

    print("\nEvery fault was handled as a STRING.")
    print("Nothing was allowed to crash the program.")