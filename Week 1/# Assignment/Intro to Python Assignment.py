# 🎉 Welcome to the Mini Calculator! 🎉
print("Welcome to the Mini Calculator! 🤖💡")
print("You can add, subtract, multiply, divide, and find the modulus of two numbers. Let's go! 🚀\n")

# 📝 Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# 📝 Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# 📝 Ask the user to choose an operation
operation = input("Enter operation (+, -, *, /, %): ")

# 🧮 Perform the selected operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("❌ Error: Division by zero is not allowed.")
elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"The result of {num1} % {num2} is {result}")
    else:
        print("❌ Error: Modulus by zero is not allowed.")
else:
    print("⚠️ Invalid Operation. Please enter +, -, *, /, or %.")

# 🎉 End of the program - Thank the user
print("\nThank you for using the Mini Calculator! 🎯 Have a great day! 😊")
