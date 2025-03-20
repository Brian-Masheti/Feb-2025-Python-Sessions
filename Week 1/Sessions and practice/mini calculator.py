# 🎉 Welcome Message
print("🎉 Welcome to the Fun Calculator! 🎉")
print("You can add, subtract, multiply, divide, find the modulus, or even calculate powers! 🚀")

# Define operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y  # Ensure that y is not 0 when calling the function.

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulus by zero is not allowed."

def power(x, y):
    return x ** y  # Handles both ** and ^ operations.

# Step 2: Map operation symbols to functions in a dictionary.
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': modulus,
    '**': power,
    '^': power  # Treats ^ as exponentiation
}

# Step 3: Ask the user for input
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %, **, ^): ")

# Step 4: Perform the operation using the dictionary.
if operation in operations:
    result = operations[operation](first_number, second_number)
    
    # Custom messages based on the operation
    if operation == '+':
        print(f"The sum of {first_number} + {second_number} is {result}")
    elif operation == '-':
        print(f"The difference of {first_number} - {second_number} is {result}")
    elif operation == '*':
        print(f"The product of {first_number} * {second_number} is {result}")
    elif operation == '/':
        print(f"The quotient of {first_number} / {second_number} is {result}")
    elif operation == '%':
        print(f"The modulus of {first_number} % {second_number} is {result}")
    elif operation in ['**', '^']:
        print(f"{first_number} raised to the power of {second_number} is {result}")
else:
    print("❌ Error: Invalid operation entered.")

# Step 5: End of the program.
print("Thank you for using the Fun Calculator! 🚀 Have a great day! 😊")
