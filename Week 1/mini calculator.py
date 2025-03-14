# Step 1: Define operation functions
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
    
# Step 2: Map operation symbols to functions in a dictionary.
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': modulus
}

# Step 3: Ask the user for input
print("🎉 Welcome to the Fun Calculator! 🎉")
print("We're going to add, subtract, multiply, and divide two numbers like a boss! 😎")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %): ")

# Step 4: Perform the operation using the dictionary.
if operation in operations:
    result = operations[operation](first_number, second_number)
    print(f'The result of {first_number} {operation} {second_number} is: {result}')
else:
    print("Error: Invalid operation entered.")

# Step 5: End of the program.
print("Thank you for using the Fun Calculator! 🚀")

