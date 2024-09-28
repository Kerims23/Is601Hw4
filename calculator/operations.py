# calculator/operations.py

import math
# Define the functions with type hints
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return the quotient of a and b. Raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def exponent(a, b):
    """Raise base to the power of exp."""
    return a ** b

def radical_expression(a, b):
    """Return the nth root of the value."""
    if a < 0 and b % 2 == 0:
        raise ValueError("Cannot take an even root of a negative number.")
    return a ** (1 / b)