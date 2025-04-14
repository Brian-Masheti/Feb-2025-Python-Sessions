# # List comprehension example

# # Traditional way to create a list

# squares = []
# for x in range(10): #
#     squares.append(x**2) # Append the square of x to the list

# print(squares)

# # List comprehension

# squares = [x**2 for x in range(10)] #

# print(squares)

# # List comprehension with condition

# even_squares = [x**2 for x in range(10) if x % 2 == 0]

# print(even_squares)

# # List comprehension with nested loops

# nested_list = [[x for x in range(3)] for y in range(3)]

# print(nested_list)

# # Complex list comprehension (less readable)

# # Example 1:
# result = [x + y for x in range(3) for y in range(3)]

# print(result)

# # Using a traditional loop for the same operation

# result = []
# for x in range(3):
#     for y in range(3):
#         result.append(x + y)

# print(result)


# # Example 2:

# result = [x * y for x in range(10) for y in range(5) if x + y > 5]

# print(result)

# Using a traditional loop for the same operation

result = []
for x in range(10):
    for y in range(5):
        if x + y > 5:
            result.append(x * y)

