"""
This is the docstring so it passes linting.
This file is to create test data to pass through main.py.
"""

import random
from calculator.operations import add, subtract, multiply, divide
from faker import Faker

fake = Faker()

# Function to generate test data with random floats for calculations
def generate_test_data(num_records):
    """
    operation mappings for calculations.
    This function creates random test data for the operations.
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for i in range(num_records):
        # Generate random float between 1 and 100
        a = random.uniform(1, 100)
        # Smaller values for division every 4th record
        b = random.uniform(1, 100) if i % 4 != 3 else random.uniform(1, 10)
        operation_name = random.choice(list(operations.keys()))
        operation_func = operations[operation_name]

        # Handling division by zero cases
        if operation_name == 'divide' and b == 0:
            expected = "ValueError"
        else:
            try:
                expected = operation_func(a, b)
            except ValueError:
                expected = "ValueError"

        yield a, b, operation_name, expected

# Add a custom pytest option to specify number of test cases
def pytest_addoption(parser):
    """
    Implements pytest option to specify the number of test cases to generate.
    """
    parser.addoption(
        "--num_records", action="store", default=5, type=int,
        help="Number of test records to generate"
    )

# Dynamically generate tests based on the generated data
def pytest_generate_tests(metafunc):
    """
    Dynamically generates test cases for pytest based on generated data.
    """
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        test_data = list(generate_test_data(num_records))
        metafunc.parametrize("a, b, operation_name, expected", test_data)
