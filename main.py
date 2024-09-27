# calculator_interactive.py
from calculator import Calculator

def main():
    while True:
        operation = input("Enter operation (+, -, *, /, 'h' for history, or 'q' to quit): ")
        if operation == 'q':
            break
        elif operation == 'h':
            print("Calculation History:")
            for entry in Calculator.get_history():
                print(entry)
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == '+':
            print(f"Result: {Calculator.add(a, b)}")
        elif operation == '-':
            print(f"Result: {Calculator.subtract(a, b)}")
        elif operation == '*':
            print(f"Result: {Calculator.multiply(a, b)}")
        elif operation == '/':
            try:
                print(f"Result: {Calculator.divide(a, b)}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid operation!")

if __name__ == "__main__":
    main()
