# Simple Calculator Program

# Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Enter operation (+, -, *, /, %): ")

# Perform the selected operation and display the result
if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '%':
    if num2 != 0:
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Error: Modulus by zero is not allowed.")
else:
    print("Invalid Operation. Please enter +, -, *, /, or %.")
