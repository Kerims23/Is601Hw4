'''docstring for pylint'''
import pytest
from main import calculate_and_print  # Ensure this import matches your project structure

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),
    # Additional test cases can be added here
    # Additional test cases for exponents
    ("2", "3", 'exponent', "The result of 2 exponent 3 is equal to 8"),
    ("5", "0", 'exponent', "The result of 5 exponent 0 is equal to 1"),
    ("-2", "3", 'exponent', "The result of -2 exponent 3 is equal to -8"),
    # Test cases for radical expressions
    ("8", "3", 'radical_expression', "The result of 8 radical_expression 3 is equal to 2"),
    ("16", "4", 'radical_expression', "The result of 16 radical_expression 4 is equal to 2"),
    ("-8", "3", 'radical_expression', "Invalid number input: -8 or 3 is not a valid number."),
    ("-8","2",'radical_expression',\
     "An error occurred: Cannot take an even root of a negative number."),
    # Edge case with non-integer root (might round depending on implementation)
    ("27", "3.0", 'radical_expression', "The result of 27 radical_expression 3.0 is equal to 3"),
    # Invalid inputs
    ("2","a",'exponent',\
     "Invalid number input: 2 or a is not a valid number."),
    ("8","-3",'radical_expression',\
     "The result of 8 radical_expression -3 is equal to 0"),  # Testing negative root
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """Test the calculate_and_print function for various operations and scenarios."""
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
