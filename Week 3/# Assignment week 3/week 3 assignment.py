# Week 3 assignment
"""
This script prompts the user to enter an item's original price and a discount percentage.
It then calculates the final price after applying the discount if the discount is 20% or higher.
If the discount is below 20%, the original price is returned.

Function Definitions:
    calculate_discount: Calculates the final price after applying the discount.
    get_user_input: Safely gets user input and prompts the user for original price and discount percentage.
"""

# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying the discount.
    
    Args:
        price (float): The original price of the item.
        discount_percent (int): The discount percentage.
        
    Returns:
        float: The final price after the discount, or the original price if the discount is below 20%.
    """
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after discount
        final_price = price - discount_amount
        return final_price, discount_amount
    else:
        # Return original price if discount is less than 20%
        return price, 0

# Function to get user input and handle potential errors
def get_user_input():
    """
    Safely prompts the user for the original price and discount percentage.
    Validates that the inputs are numbers.
    """
    while True:
        try:
            # Prompt the user for the original price
            original_price = float(input("Enter the original price of the item: "))
            # Prompt the user for the discount percentage
            discount_percent = float(input("Enter the discount percentage: "))
            # Check if the discount percentage is valid (between 0 and 100)
            if discount_percent < 0 or discount_percent > 100:
                print("Invalid discount percentage. Please enter a value between 0 and 100.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate and display the result
    final_price, discount_amount = calculate_discount(original_price, discount_percent)

    # Print the result with appropriate message
    print("\n=== Price Calculation Summary ===")
    print(f"Original Price: ${original_price:.2f}")
    print(f"Discount Percentage: {discount_percent}%")

    if discount_percent >= 20:
        print(f"Discount Amount: ${discount_amount:.2f}")
        print(f"Final Price After {discount_percent}% Discount: ${final_price:.2f}")
    else:
        print("Note: Discount is less than 20%")
        print("No discount applied.")
        print(f"Final Price: ${final_price:.2f}")

# Main execution part (start of the program)
if __name__ == "__main__":
    get_user_input()