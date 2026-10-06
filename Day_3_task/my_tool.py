import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


def calculator(expression):
    try:
        tree = ast.parse(expression, mode="eval")

        def evaluate(node):
            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value
                raise ValueError("Only numbers are allowed.")

            if isinstance(node, ast.BinOp):
                left = evaluate(node.left)
                right = evaluate(node.right)

                operation = OPERATORS.get(type(node.op))

                if operation is None:
                    raise ValueError("Operator not allowed.")

                return operation(left, right)

            raise ValueError("Invalid expression.")

        return str(evaluate(tree.body))

    except Exception as e:
        return "Calculation failed: " + str(e)


TOOL = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Perform a basic arithmetic calculation.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Arithmetic expression to calculate."
                }
            },
            "required": ["expression"]
        }
    }
}


if __name__ == "__main__":
    print(calculator("12000 + 18000"))