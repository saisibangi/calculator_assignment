# Basic Calculator Program
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed!"
    else:
        return "Invalid operation. Please enter +, -, * or /."

    return f"{num1} {operation} {num2} = {result}"

# Run the calculator
print(calculator())