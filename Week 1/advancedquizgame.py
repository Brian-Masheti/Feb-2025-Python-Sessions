import time
import random

# Define quiz questions for different categories
quiz_categories = {
    "Python": [
        {"question": "What is the keyword to define a function in Python?", 
         "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},
        {"question": "What does `print(2 ** 3)` output in Python?", 
         "options": ["A) 5", "B) 6", "C) 8", "D) 9"], "answer": "C"},
        {"question": "Which data type is mutable in Python?", 
         "options": ["A) Tuple", "B) String", "C) List", "D) Integer"], "answer": "C"}
    ],
    
    "Movies": [
        {"question": "Which movie won Best Picture at the 2023 Oscars?", 
         "options": ["A) Avatar 2", "B) Everything Everywhere All at Once", "C) Top Gun: Maverick", "D) The Batman"], "answer": "B"},
        {"question": "Who played Iron Man in the Marvel Cinematic Universe?", 
         "options": ["A) Chris Evans", "B) Chris Hemsworth", "C) Robert Downey Jr.", "D) Mark Ruffalo"], "answer": "C"},
        {"question": "Which animated film features a song called 'Let It Go'?", 
         "options": ["A) Moana", "B) Tangled", "C) Frozen", "D) Encanto"], "answer": "C"}
    ],
    
    "General Knowledge": [
        {"question": "What is the capital of France?", 
         "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
        {"question": "How many continents are there?", 
         "options": ["A) 5", "B) 6", "C) 7", "D) 8"], "answer": "C"},
        {"question": "Which planet is known as the Red Planet?", 
         "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "B"}
    ]
}

def quiz():
    score = 0

    # Let user choose a category
    print("\nChoose a category:")
    for i, category in enumerate(quiz_categories.keys(), 1):
        print(f"{i}. {category}")

    choice = int(input("Enter the number of your choice: "))
    category_name = list(quiz_categories.keys())[choice - 1]

    print(f"\n📝 Starting {category_name} Quiz...\n")

    # Select random 3 questions from the chosen category
    questions = random.sample(quiz_categories[category_name], 3)

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        # Start timer
        start_time = time.time()
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        elapsed_time = time.time() - start_time

        # Check if time exceeded
        if elapsed_time > 10:
            print("⏳ Time's up! No points for this question.")
            continue

        # Check if answer is correct
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    # Display final score
    print(f"\n🎉 You scored {score} out of 3!")

# Loop to allow replaying
while True:
    quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 🎯")
        break
