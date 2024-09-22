def add(a:float, b:float) -> float:
    result = a + b
def subtract(a:float, b:float) -> float:
    result = a - b 
def multiply(a:float, b:float) -> float:
    result = a * b
def divide(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    result = a / b