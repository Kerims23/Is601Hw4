# calculator_interactive.py
from calculator import add, subtract, multiply, divide

def main():
    while True:
        operation = input("Enter operation (+, -, *, / or 'q' to quit): ")
        if operation == 'q':
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == '+':
            print(f"Result: {add(a, b)}")
        elif operation == '-':
            print(f"Result: {subtract(a, b)}")
        elif operation == '*':
            print(f"Result: {multiply(a, b)}")
        elif operation == '/':
            try:
                print(f"Result: {divide(a, b)}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid operation!")

if __name__ == "__main__":
    main()
