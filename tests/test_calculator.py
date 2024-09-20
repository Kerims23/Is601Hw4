# tests/test_calculator.py
'''I think I need a docstring here ? '''

from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works'''    
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works'''    
    assert subtract(2, 2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2, 3) == 6

def test_division():
    '''Test that division function works'''
    assert divide(6, 2) == 3

def test_divide_by_zero():
    '''Test that division by zero raises an error'''
    try:
        divide(6, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
