import ast
import operator as op


# College canteen food prices
FOOD_PRICES = {
    "idly": 30,
    "dosa": 50,
    "fried_rice": 80
}


# Tool 1: Get food price
def get_food_price(food_name, meal_type):
    if food_name not in FOOD_PRICES:
        raise ValueError(
            f"Unknown food: {food_name}. "
            f"Valid foods: {', '.join(FOOD_PRICES.keys())}"
        )

    return FOOD_PRICES[food_name]


# Safe calculator
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv
}


def safe_calculator(expression):
    tree = ast.parse(expression, mode="eval")

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return ALLOWED_OPERATORS[type(node.op)](left, right)

        raise ValueError("Unsupported expression")

    return evaluate(tree)


# Tool 2: Calculate bill
def calculate_bill(expression):
    return safe_calculator(expression)


# Tool functions available to the agent
TOOL_FUNCTIONS = {
    "get_food_price": get_food_price,
    "calculate_bill": calculate_bill,
}


# JSON Schemas sent to the model
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_food_price",
            "description": "Get the price of a food item from the college canteen.",
            "parameters": {
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
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_bill",
            "description": "Calculate a canteen bill using a simple arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"],
                "additionalProperties": False
            }
        }
    }
]


# Same schemas used by our validator
SCHEMAS = {
    "get_food_price": TOOLS[0]["function"]["parameters"],
    "calculate_bill": TOOLS[1]["function"]["parameters"],
}


if __name__ == "__main__":
    print("Dosa price:", get_food_price("dosa", "lunch"))
    print("Bill:", calculate_bill("50 + 80"))