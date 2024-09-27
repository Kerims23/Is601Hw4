import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """Generate test data for various arithmetic operations."""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    for _ in range(num_records):
        a = fake.random_number(digits=2)
        b = fake.random_number(digits=2) if _ % 4 != 3 else fake.random_number(digits=1)
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Handle division by zero case
        if operation_func == divide and b == 0:
            expected = "ZeroDivisionError"
        else:
            expected = operation_func(a, b) if operation_func != divide else operation_func(a, b)

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Add command-line options for pytest."""
    parser.addoption("--num_records", action="store", default=5, type=int,
                     help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate tests dynamically based on available fixtures."""
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
                               for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
