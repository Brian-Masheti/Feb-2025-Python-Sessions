# Write files in write mode
with open('ouput.txt', 'w') as file:
    # write to the file
    file.write('Hello, Python,!, This is a test file.\n')
    file.write('You only have a single attempt.\n')
    print('File written successfully.')

# append to a file
with open('ouput.txt', 'a') as file:
    # append to the file
    file.write('This is an appended line.\n')
    print('File appended successfully.')
