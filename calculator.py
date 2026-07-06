# calculator.py
# This file contains intentional code quality issues for demo purposes

def calculate(a, b, operation, **kwargs):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        a: First operand
        b: Second operand
        operation: Operation to perform ('add', 'subtract', 'multiply', 'divide')
        **kwargs: Additional parameters (not used in current implementation)
        
    Returns:
        Result of the operation
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None
    }
    
    if operation in operations:
        return operations[operation](a, b)
    else:
        raise ValueError(f"Unsupported operation: {operation}")