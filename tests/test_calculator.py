# tests/test_calculator.py
'''
I think I need a docstring here ? 
# line below no longer needed because we have a class now :) 
# from calculator import add, subtract, multiply, divide
# '''

from calculator import Calculator
def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert Calculator.subtract(2, 2) == 0

def test_multiplication():
    '''Test that multiplication function works '''    
    assert Calculator.multiply(2, 2) == 4

def test_division():
    '''Test that division function works '''    
    assert Calculator.divide(4, 2) == 2

def test_divide_by_zero():
    '''Test division by zero raises an exception'''
    try:
        Calculator.divide(4, 0)
    except ValueError:
        assert True
    else:
        assert False
