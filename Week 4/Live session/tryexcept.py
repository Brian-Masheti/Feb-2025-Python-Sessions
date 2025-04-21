# Exception handling in Python
# Exception handling in Python is done using try, except, and finally blocks.

try:
    with open('test.txt', 'r') as f: # Althouggh if the file exists, it will be opened in read mode.
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the file path.")

