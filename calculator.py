# calculator.py
# This file contains intentional code quality issues for demo purposes

import os
import sys  # unused import — S1128

PASSWORD = "admin123"  # hardcoded credential — S2068

def calculate(a, b, operation, extra1=None, extra2=None, extra3=None,
              extra4=None, extra5=None, extra6=None):  # too many params — S107
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
        if b == 0:
            return None
        result = a / b
    elif operation == "power":
        result = a ** b
    elif operation == "modulo":
        result = a % b
    elif operation == "floor_divide":
        result = a // b
    else:
        result = 0

    if result > 100:
        if result > 200:
            if result > 300:
                if result > 400:
                    print("very large")  # deep nesting — S3776
    return result


def unused_function(x, y, z):  # unused parameters — S1172
    return 42


def get_user_data(user_id):
    data = {"id": user_id, "name": "test"}
    data = {"id": user_id, "name": "updated"}  # variable reassigned before use — S1854
    return data


x = 1 + 1  # result not used — S905
