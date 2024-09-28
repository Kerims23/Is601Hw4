'''My Calculator Test'''
import pytest
from calculator import Calculator

def test_addition():
    '''Test that addition function works.'''
    assert Calculator.add(2, 2) == 4
    assert Calculator.add(-1, 1) == 0  # Edge case
    assert Calculator.add(0, 0) == 0   # Edge case
    assert Calculator.add(2.5, 2.5) == 5.0  # Testing with floats

def test_subtraction():
    '''Test that subtraction function works.'''
    assert Calculator.subtract(2, 2) == 0
    assert Calculator.subtract(5, 3) == 2  # Edge case
    assert Calculator.subtract(-1, 1) == -2  # Edge case
    assert Calculator.subtract(0, 0) == 0   # Edge case

def test_division():
    '''Test that division function works.'''
    assert Calculator.divide(2, 2) == 1
    assert Calculator.divide(5, 2) == 2.5  # Testing with floats
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(2, 0)  # Edge case: division by zero

def test_multiplication():
    '''Test that multiplication function works.'''
    assert Calculator.multiply(2, 2) == 4
    assert Calculator.multiply(0, 5) == 0   # Edge case
    assert Calculator.multiply(-1, 5) == -5  # Edge case
    assert Calculator.multiply(2.5, 2) == 5.0  # Testing with floats

def test_exponent():
    assert Calculator.exponent(2, 3) == 8

def test_radical_expression():
    assert Calculator.radical_expression(8, 3) == 2
    assert Calculator.radical_expression(16, 4) == 2
    with pytest.raises(ValueError):
        Calculator.radical_expression(-8, 2)  # Error for even root of negative number
