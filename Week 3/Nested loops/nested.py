Nested loops example

for i in range(1, 4): # Outer loop
    for j in range(1, 4): # Inner loop
        print(f"i = {i}, j = {j}") #

The outer loop runs 3 times (i = 1, 2, 3)
The inner loop runs 3 times (j = 1, 2, 3)
The inner loop runs 3 times for each iteration of the outer loop
The inner loop runs 3 * 3 = 9 times


# Nested loops with a break statement

for i in range(1, 4): # Outer loop
    for j in range(1, 4): # Inner loop
        if i == 2 and j == 2: # Check if i is 2 and j is 2
            break # Break the inner loop
        print(f"i = {i}, j = {j}") # Print the values of i and j

# The break statement stops the inner loop when i is 2 and j is 2
# The outer loop continues to run because the break statement is inside the inner loop


# Nested loops with a continue statement

for i in range(1, 4): # Outer loop
    for j in range(1, 4): # Inner loop
        if i == 2 and j == 2: # Check if i is 2 and j is 2
            continue # Skip the rest of the inner loop
        print(f"i = {i}, j = {j}") # Print the values of i and j




