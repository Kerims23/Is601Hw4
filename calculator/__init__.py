# Inside calculator/__init__.py

class Calculator:
    history = []
    
    @staticmethod
    def add(a, b):
        result = a + b
        Calculator.history.append(result)
        return result
    
    @staticmethod
    def subtract(a, b):
        result = a - b
        Calculator.history.append(result)
        return result

    @staticmethod
    def multiply(a, b):
        result = a * b
        Calculator.history.append(result)
        return result
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(result)
        return result

    @classmethod
    def get_history(cls):
        return cls.history
