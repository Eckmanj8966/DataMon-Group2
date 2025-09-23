# Memory Bank

question_bank = [] # empty list to hold all the questions

# a function to add questions and their answers
def add_question():
    
    # get the question and answer from the user
    question = input("Enter your math question: (eg., 'What is 5 + 3?') ")
    answer = input("Enter the correct answer: ")
    
    # package them so each question is matched with its answer
    question_data = {
        'question': question,
        'answer': answer
    }
    
    # put in storage
    question_bank.append(question_data)
    
    '''
    What get's stored?
    
    Question: "What is 7 + 5?"
    Answer: 12
    
    {'question': 'What is 7 + 5?', 'answer': '12'}
    '''
    
    # let the user know
    print("Your question has been stored!")
    print(f'Total questions in bank: {len(question_bank)}')

# a function to view all the questions stored
def view_all_questions():
    if len(question_bank) == 0:
        print("\nNo questions have been stored yet!")
        return
    
    print(f"\n ALL STORED QUESTIONS ({len(question_bank)} total)")
    for i in range(len(question_bank)):
        q = question_bank[i]
        print(f"{i+1}. {q['question']}")
        print(f"   Answer: {q['answer']}")
        print()
        
# a function that allows the user to solve the stored question
def solve_question():
    if len(question_bank) == 0:
        print("\nNo questions to solve yet! Add some questions first.")
        return
    
    print("\n=== SOLVE QUESTIONS ===")
    print(f"You have {len(question_bank)} questions to solve!")
    
    # Keep track of score
    correct = 0
    total = 0
    
    # Go through each question
    for i in range(len(question_bank)):
        q = question_bank[i]
        total = total + 1
        
        print(f"\nQuestion {i+1}: {q['question']}")
        user_answer = input("Your answer: ")
    
        # Check if correct (convert both to strings to compare)
        if user_answer.strip() == q['answer'].strip():
            print("✓ Correct!")
            correct = correct + 1
        else:
            print(f"✗ Wrong! The correct answer is: {q['answer']}")
    
    # Show final score
    print("\n=== FINAL SCORE ===")
    print(f"You got {correct} out of {total} questions correct!")
    if correct == total:
        print("🎉 Perfect score! Great job!")
    elif correct >= total / 2:
        print("👍 Good job! Keep practicing!")
    else:
        print("📚 Keep studying! You'll do better next time!")
    
def menu():
    print("\n" + "="*30)
    print("MEMORY BANK")
    print("="*30)
    print(f"Questions stored: {len(question_bank)}")
    print("\n1) Add a question")
    print("2) View all questions")
    print("3) Solve questions (Quiz Mode)")
    print("4) Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        add_question()
        menu()  # Go back to menu
    elif choice == "2":
        view_all_questions()
        menu()  # Go back to menu
    elif choice == "3":
        solve_question()
        menu()  # Go back to menu
    elif choice == "4":
        print("Goodbye!")
        return  # Exit
    else:
        print("Invalid choice! Please try 1, 2, 3, or 4.")
        menu()
        
def main():
    print("Welcome to the Memory Bank!")
    menu()
        
if __name__ == '__main__':
    main()