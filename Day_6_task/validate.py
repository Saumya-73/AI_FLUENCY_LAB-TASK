from tools import SCHEMAS


def validate_arguments(tool_name, arguments):
    # Check whether tool exists
    if tool_name not in SCHEMAS:
        return f"Unknown tool: {tool_name}"

    schema = SCHEMAS[tool_name]

    # Arguments must be a dictionary
    if not isinstance(arguments, dict):
        return "Arguments must be a JSON object."

    properties = schema.get("properties", {})
    required = schema.get("required", [])

    # Check missing required arguments
    for name in required:
        if name not in arguments:
            return f"Missing required argument '{name}'."

    # Check extra arguments
    for name in arguments:
        if name not in properties:
            return f"Unexpected argument(s): {name}."

    # Check argument types
    for name, value in arguments.items():
        expected_type = properties[name].get("type")

        if expected_type == "string" and not isinstance(value, str):
            return (
                f"Argument '{name}' must be a string, "
                f"but got {type(value).__name__}: {value}."
            )

    # Check enum values
    for name, value in arguments.items():
        allowed_values = properties[name].get("enum")

        if allowed_values and value not in allowed_values:
            return (
                f"Argument '{name}' must be one of "
                f"{allowed_values}, got '{value}'."
            )

    return None


if __name__ == "__main__":
    tests = [
        ("get_food_price", {"food_name": "dosa", "meal_type": "lunch"}),
        ("get_food_price", {"food_name": "dosa"}),
        ("get_food_price", {"food_name": "dosa", "meal_type": "brunch"}),
        ("get_food_price", {"food_name": "dosa", "meal_type": "lunch", "year": 2026}),
        ("get_food_price", {"food_name": 123, "meal_type": "lunch"}),
    ]

    for tool_name, arguments in tests:
        result = validate_arguments(tool_name, arguments)

        if result is None:
            result = "OK"

        print(arguments, "->", result)