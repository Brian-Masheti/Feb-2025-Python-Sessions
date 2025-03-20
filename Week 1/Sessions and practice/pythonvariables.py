# Assigning values to variables
site_name = "Python Programming"
print(site_name)


# Changing variable names
site_name = "I ❤️  Love coding with Python" # ASsigning new name to site_name
print(site_name)

# Assigning multiple values to multiple variables
a, b, c = 5, 3.2, "Hello"
print(a)
print(b)
print(c)

# Rulues for naming variables
# A variable name must start with a letter or the underscore character
# Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_)
# Spaces are not allowed in variable names. Use underscores instead to represent spaces. E.g., first_name, last_name

num = 5
Num = 10

# Python is case-sensitive, hence num and Num are different variables.

################################################################################################################################


# Python Data Types
# Python has five standard data types − numeric, string, sequence, mapping, boolean, and set.

# We can use the type() function to know which class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class.

# Numeric Data Type

num1 = 5
num2 = 3.14
print(type(num1))
print(type(num2))

# List Data Type
# List is an ordered sequence of items. It is one of the most used data types in Python and is very flexible. All the items in a list do not need to be of the same type.

languages = ['Python', 'Java', 'C++', 'French', 'C', 'JavaScript', 23, 'Web Development', 3.14]
print(type(languages))

## Accessing List items
print(languages[0]) # Output: Python
print(languages[1]) # Output: Java
print(languages[-3]) # Output: 23


# Tuple Data Type
# Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
# Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

product = ('Mobile 📞', 5000, 'Samsung 📱', 5.5)
print(type(product))
print(product[2]) # Output: Samsung

# String Data Type
# String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings.

name = 'Python Programming'
print(type(name))

# Set data type
# Set is an unordered collection of unique items. Set is defined by values separated by a comma inside braces { }. Items in a set are not ordered.

capital_cities = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'UK': 'London', 'France': 'Paris'}
print(capital_cities)
print(type(capital_cities))