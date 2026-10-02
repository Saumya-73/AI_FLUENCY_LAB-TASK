def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Calculation failed: " + str(e)