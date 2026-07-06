# calculator.py
# This file contains intentional code quality issues for demo purposes

import os  # unused import — S1128

PASSWORD = "admin123"  # hardcoded credential — S2068

def calculate(a, b, operation, extra1=None, extra3=None,
              extra4=None, extra5=None, extra6=None):  # too many params — S107
    # Commented-out code block — S125
    # result = a + b
    # print(result)

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":