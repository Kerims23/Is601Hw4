'''My Calculator Test'''

# Correct the import order by placing standard library imports before third-party library imports,
# adhering to PEP 8 guidelines for import ordering.
from decimal import Decimal
import pytest

# Import Calculation and Calculations classes from the calculator package,
# assuming these are the correct paths following Python's package and module naming conventions.
from calculator.calculation import Calculation
from calculator.transactions import Calculations

# Import arithmetic operation functions (add and subtract) to be tested.
from calculator.operations import add, subtract

# pytest.fixture is a decorator that marks a function as a fixture,
# a setup mechanism used by pytest to initialize a test environment.
# Here, it's used to define a fixture that prepares the test environment for calculations tests.
@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"

def test_find_by_invalid_operation(setup_calculations):
    """Test finding calculations in the history by an invalid operation type."""
    invalid_operations = Calculations.find_by_operation("multiply")
    assert len(invalid_operations) == 0, "Expected no calculations for invalid operation"
    