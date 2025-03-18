# Data structures
# Data structures are a way of organizing and storing data so that they can be accessed and worked with efficiently. 
# They define the relationship between the data, and the operations that can be performed on the data.
# In this section, we will cover some of the most common data structures used in Python, including lists, tuples, sets, and dictionaries.

# Lists
# A list is a collection of items that are ordered and changeable. 
# Lists are defined by enclosing the items in square brackets (`[]`), separated by commas. 
# Lists can contain items of different types, including other lists. Lists are mutable, which means that you can change the items in a list by assigning new values to them. 
# You can also add and remove items from a list, and concatenate lists together. 
# Lists are indexed, which means that you can access individual items in a list by their position. 
# Lists are a versatile and powerful data structure that can be used in a wide variety of applications.
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [1, 'a', 2, 'b', 3, 'c']

# Tuples
# A tuple is a collection of items that are ordered and unchangeable. 
# Tuples are defined by enclosing the items in parentheses (()), separated by commas. 
# Tuples can contain items of different types, including other tuples. 
# Tuples are immutable, which means that you cannot change the items in a tuple once it has been created. 
# You can, however, access individual items in a tuple by their position. 
# Tuples are useful for storing data that should not be changed, such as the coordinates of a point in space or the RGB values of a color.

tuple1 = (1, 2, 3, 4, 5)
students = ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Daisy')
print(students[0])  # Output: Alice
print(students[-3])  # Output: David

# Dictonaries
# A dictionary is an ordered collection of items that are unordered, changeable, and indexed. 
# Dictionaries are defined by enclosing the items in curly braces (`{}`), separated by commas, and each item is a key-value pair. 
# The key is used to access the value associated with it. Dictionaries are mutable, which means that you can change the items in a dictionary by assigning new values to them. You can also add and remove items from a dictionary. 
# Dictionaries are useful for storing data in a structured way, where each item has a unique key that can be used to access it.
student = {
    'name': 'Alice',
    'age': 20,
    'gender': 'Female',
    'is_student': True,
    'courses': ['Math', 'Science', 'English'],
    'GPA': 3.5
}

# Append new key-value pair to the dictionary
student['height'] = 5.5

print(student)
print(student['age'])  # Output: 20
print(student['courses'], student['GPA'])  # Output: ['Math', 'Science', 'English'] 3.5

# countries with their capital cities
countries = {
    'USA': 'Washington D.C.',
    'UK': 'London',
    'France': 'Paris',
    'Germany': 'Berlin'
}
 
print(countries)

# Sets
# A set is an unordered collection of unique items. Sets are defined by enclosing the items in curly braces (`{}`), separated by commas. 
# Sets can contain items of different types, but they cannot contain duplicate items. 
# Sets are mutable, which means that you can add and remove items from a set. 
# Sets are useful for storing data in a way that ensures that each item is unique. 
# Sets can be used to perform set operations such as union, intersection, difference, and symmetric difference.

student_ids = {1, 2, 3, 4, True, 'John'} # True and false are considered as 1 and 0 respectively therefore the output will not output true.
print(student_ids)  # Output: {True, 101, 102, 103, 104, 105}
