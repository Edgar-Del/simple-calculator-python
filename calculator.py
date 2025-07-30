"""
Simple Calculator in Python
Program that asks the user to input two numbers and a mathematical operation,
performs the operation and displays the result.
"""

def main():
    print("=== Simple Calculator ===")
    print("Available operations: +, -, *, /")
    print()
    
    # Ask for the first number
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Ask for the second number
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Ask for the operation
    operation = input("Enter the operation (+, -, *, /): ").strip()
    
    # Perform the operation based on user input
    result = None
    
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Invalid operation. Use +, -, *, or /.")
        return

if __name__ == "__main__":
    main() 