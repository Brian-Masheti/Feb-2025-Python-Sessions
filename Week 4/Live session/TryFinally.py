# Advanced Error Handling with `finally` and Custom Erros 

# This script demonstrates the use of try, except, and finally blocks in Python.

# Example with finally block - fixed version
file = None  # Initialize file variable to None
try:
    file = open('sample.txt', 'r')  # Attempt to open a file in read mode
    data = file.read()  # Read the contents of the file
    print(data)
except FileNotFoundError:
    print('File not Found.')
    print('Operation Completed')
finally:
    if file is not None:  # Only close the file if it was successfully opened
        file.close()


# Example with custom error handling
# class CustomError(Exception):
try:
    # Attempt to open a file in read mode
    with open('sample.txt', 'r') as file:
        # Read the contents of the file
        data = file.read()
        print(data)
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("File not found. Please check the file path.")
finally:
    # This block executes regardless of whether an exception occurred
    print("File operation completed.")



"""
    Best Practices
    - Use `with` fr file andling: Auto-close files, preventing potential leaks.
    - CHeck file existance before reading/writing, to avoid crashes.
    - Handle specifiexceptions over general ones (e.g., `FileNotFoundError` instead of `Exception`).
"""