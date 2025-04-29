# Import the entire math library
import math
import random
import requests
print(math.sqrt(16)) # 4.0

# mport a single module from the math library
# from math import sqrt

# print(sqrt(16)) # 4.0

print('Sine of 90 degrees:', math.sin(math.radians(90))) # 1.0
print('Cosine of 0 degrees:', math.cos(math.radians(0))) # 1.0


# Find the power of a number
print('Power of 2^3:', math.pow(2, 3)) # 8.0
# print('Power of 2^3:', 2**3) # 8.0    # Altenative way to find power
print('The power of 2^9.5:', math.pow(2, 9.5)) # 724.0773439350247


# Print a Random Number
print('Random number between 1 and 12:', random.randint(1, 12))

# Random choice from a list of food items
food_items = ['Pizza', 'Burger', 'Pasta', 'Salad', 'Sushi']
print('Random food item:', random.choice(food_items)) # Randomly selects a food item from the list

print("Random Girls' Name:", random.choice(['Alice', 'Emma', 'Sophia', 'Olivia'])) # Randomly selects

