# calculator/operations.py

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

def square_root(a: float) -> float:
    """Return the square root of a. Raise ValueError if a is negative."""
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return a ** 0.5  # Using exponentiation to calculate the square root

def exponentiate(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return base ** exponent  # Using exponentiation
