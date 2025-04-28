# Python provies multiple ways to read file conetents:
# 1. read() - reads the entire file.
# 2. readline() - reads a single line at a time.
# 3. readlines() - reads all lines and returns a list of lines.
# 4. read(size) - reads a specified number of bytes from the file.



# open files in read mode
with   open('./Live session/example.txt', 'r') as file:
    # read the contents of the file
    content = file.read()
    print(content)


# open a file and read a single line 
with open('./Live session/example.txt', 'r') as file:
    content = file.readline() # read a single line
    # content = file.readlines() # read all lines into a list
    print(content)


# Write files in write mode
with open('ouput.txt', 'w') as file:
    # write to the file
    file.write('Hello, Python,!, this is a test file.\n')
    file.write('You only have a single attempt.\n')
    print('File written successfully.')



