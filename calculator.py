# calculator.py
# This file contains intentional code quality issues for demo purposes

def calculate(a, b, operation, **kwargs):
    # Commented-out code block — S125
    # result = a + b
    # print(result)

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b != 0:
            result = a / b
        else:
            raise ValueError("Cannot divide by zero")
    elif operation == "power":
        result = a ** b
    elif operation == "modulo":
        if b != 0:
            result = a % b
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError(f"Unsupported operation: {operation}")
    
    return result