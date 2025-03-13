def quiz():
    score = 0
    
    questions = [
        {
            "question": "What is the keyword to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "Which movie won the Oscar for Best Picture in 2023?",
            "options": ["A) Avatar: The Way of Water", "B) Everything Everywhere All at Once", "C) Top Gun: Maverick", "D) The Batman"],
            "answer": "B"
        },
        {
            "question": "What does `print(2 ** 3)` output in Python?",
            "options": ["A) 5", "B) 6", "C) 8", "D) 9"],
            "answer": "C"
        }
    ]
    
    # Loop through each question
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        # Get user's answer
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        # Check if the answer is correct
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    # Display final score
    print(f"\n🎉 You got {score} out of {len(questions)} correct!")

# Loop to allow replaying
while True:
    quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 🎯")
        break
