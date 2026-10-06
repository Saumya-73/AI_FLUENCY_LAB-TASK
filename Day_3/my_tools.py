import ast
import operator
import os
import re

# ---------- Calculator ----------

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
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


# ---------- Webpage Reader ----------

def read_webpage(url, max_chars=2000):
    try:
        if url.startswith("http://") or url.startswith("https://"):
            import requests

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            html = response.text
        else:
            if url.startswith("file:///"):
                url = url[8:]

            with open(url, "r", encoding="utf-8") as file:
                html = file.read()

        # Remove script and style sections
        html = re.sub(
            r"<(script|style).*?>.*?</\1>",
            "",
            html,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Remove HTML tags
        text = re.sub(r"<[^>]+>", " ", html)

        # Clean extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        return text[:max_chars]

    except Exception as e:
        return "Error reading webpage: " + str(e)


# ---------- Tool Registry ----------

TOOL_FUNCTIONS = {
    "calculator": calculator,
    "read_webpage": read_webpage,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform arithmetic calculations.",
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
    },
    {
        "type": "function",
        "function": {
            "name": "read_webpage",
            "description": "Read a webpage or local HTML file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL or local HTML file path."
                    }
                },
                "required": ["url"]
            }
        }
    }
]


if __name__ == "__main__":
    print("Calculator test:")
    print(calculator("12000 + 18000"))

    print("\nWebpage test:")
    print(read_webpage("Day_3/notice.html"))