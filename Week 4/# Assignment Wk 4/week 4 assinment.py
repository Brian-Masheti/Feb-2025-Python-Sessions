#* **File Read & Write Challenge** ✏️: Create a program that reads a file and writes a modified version to a new file.

def add_line_numbers(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            # Read all lines from the file
            lines = input_file.readlines()
            
        # Open the output file for writing
        with open(output_filename, 'w') as output_file:
            # Write each line with line number
            for line_num, line in enumerate(lines, 1):
                output_file.write(f"{line_num}: {line}")
                
        print(f"Successfully processed {input_filename} and created {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    add_line_numbers("text.txt", "numbered_text.txt")


# * **Error Handling Lab** 🧪: Ask the user for a filename and handle errors if it doesn't exist or can't be read.
def read_user_file():
    while True:
        filename = input("Enter the name of the file you want to read: ")
        
        try:
            # Try to open and read the file
            with open(filename, 'r') as file:
                contents = file.read()
                print("\nFile contents:")
                print("-------------")
                print(contents)
                print("-------------")
                break  # Exit the loop if file is successfully read
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            retry = input("Would you like to try again? (y/n): ")
            if retry.lower() != 'y':
                print("Operation cancelled.")
                break
                
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'.")
            retry = input("Would you like to try again? (y/n): ")
            if retry.lower() != 'y':
                print("Operation cancelled.")
                break
                
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            retry = input("Would you like to try again? (y/n): ")
            if retry.lower() != 'y':
                print("Operation cancelled.")
                break

# Run the function if this script is executed
if __name__ == "__main__":
    read_user_file()
