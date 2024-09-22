'''Testing Operations'''
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    '''Testing the addition operation'''
    assert add(10.5, 5.5) == 16.0, "Add operation failed"
    assert add(0.0, 0.0) == 0.0, "Add operation failed with zero"

def test_operation_subtract():
    '''Testing the subtract operation'''
    assert subtract(10.0, 5.0) == 5.0, "Subtract operation failed"
    assert subtract(5.0, 10.0) == -5.0, "Subtract operation failed for negative result"

def test_operation_multiply():
    '''Testing the multiply operation'''
    assert multiply(10.0, 5.0) == 50.0, "Multiply operation failed"
    assert multiply(0.0, 10.0) == 0.0, "Multiply operation failed with zero"

def test_operation_divide():
    '''Testing the divide operation'''
    assert divide(10.0, 2.0) == 5.0, "Divide operation failed"
    assert divide(5.0, 2.0) == 2.5, "Divide operation failed with float result"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10.0, 0.0)
