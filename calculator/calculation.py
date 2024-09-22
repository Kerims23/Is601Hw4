# calculator/calculation.py

from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """
    A class to represent a mathematical calculation, encapsulating two operands and an operation.
    """
    
    def __init__(self, a: float, b: float, operation):
        """
        Initialize the calculation with two operands and an operation.
        
        :param a: The first operand.
        :param b: The second operand.
        :param operation: The operation function (e.g., add, subtract).
        """
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod
    def create(a: float, b: float, operation):
        """
        Static method to create a Calculation object.
        
        :param a: The first operand.
        :param b: The second operand.
        :param operation: The operation function.
        :return: A new Calculation object.
        """
        return Calculation(a, b, operation)

    def perform(self) -> float:
        """
        Perform the calculation and return the result.
        
        :return: The result of the calculation.
        """
        return self.operation(self.a, self.b)

    def __repr__(self):
        """
        Provide a string representation of the Calculation object for debugging.
        
        :return: A string representation of the Calculation.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
