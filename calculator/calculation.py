# calculator/calculation.py

from typing import Callable  # Import Callable for type hinting of operations
from calculator.operations import add, subtract, multiply, divide  # Import arithmetic operations

class Calculation:
    """Represents a calculation involving two operands and an operation."""

    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        """
        Initialize a Calculation instance.

        Parameters:
        a (float): The first operand.
        b (float): The second operand.
        operation (Callable): The operation to perform on the operands.
        """
        self.a = a  # First operand
        self.b = b  # Second operand
        self.operation = operation  # Callable operation

    @staticmethod    
    def create(a: float, b: float, operation: Callable[[float, float], float]) -> 'Calculation':
        """
        Create a new Calculation instance.

        Parameters:
        a (float): The first operand.
        b (float): The second operand.
        operation (Callable): The operation to perform.

        Returns:
        Calculation: A new instance of Calculation.
        """
        return Calculation(a, b, operation)

    def perform(self) -> float:
        """Perform the calculation and return the result."""
        return self.operation(self.a, self.b)  # Call the operation with operands

    def __repr__(self) -> str:
        """Return a string representation of the Calculation instance."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"  # Readable output
