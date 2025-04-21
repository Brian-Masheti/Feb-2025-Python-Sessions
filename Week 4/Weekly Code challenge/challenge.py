def process_text_file():
    try:
        # Step 1: Read the input file
        with open('input.txt', 'r') as file:
            content = file.read()
        
        # Step 2: Process the content
        # Convert to uppercase
        uppercase_content = content.upper()
        # Count words (split by whitespace)
        word_count = len(content.split())
        
        # Step 3: Write to output file
        with open('output.txt', 'w') as file:
            file.write("=== Processed Content ===\n")
            file.write(uppercase_content)
            file.write("\n\n=== Statistics ===\n")
            file.write(f"Total words: {word_count}\n")
        
        # Step 4: Print success message
        print("✅ Success! The file has been processed.")
        print(f"📝 Total words processed: {word_count}")
        print("📄 Results have been written to output.txt")
        
    except FileNotFoundError:
        print("❌ Error: input.txt not found. Please create the input file first.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

# Run the function
if __name__ == "__main__":
    process_text_file()
