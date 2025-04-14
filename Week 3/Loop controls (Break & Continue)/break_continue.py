# Example of loop controls: break and continue

for number in range(1, 10): # Loop through numbers 1 to 9
    if number == 5: # Check if the number is 5
        print('Breaking the loop at 5')
        break # Break the loop when the number is 5
    elif number %2 == 0:
        print(f"Skipping {number} because it's even")
        continue # Skip the rest of the loop for even numbers
    print(f"Processing number: {number}")

# Break: stops the loopentirely when the number == 5.
# continue: Skips the current iteration when `number` is even and moves to the next loop iteration.

# Example of using break and continue in a while loop

count = 0

while count < 10: # Loop will continue until count is equal to or less than 9
    count += 1 # Increment the count by 1
    if count %2 == 0: # Check if the count is even
        print(f"Skipping {count} because it's even")
        continue # Skip the rest of the loop for even numbers
    print(f"Processing number: {count}")

