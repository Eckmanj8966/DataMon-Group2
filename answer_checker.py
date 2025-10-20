def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def get_int_choice(prompt, min_choice, max_choice):
    while True:
        try:
            choice = int(input(prompt))
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a number between {min_choice} and {max_choice}.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def answer_checker():
    print("\nPlease choose the problem type of your choice:")
    print("1) Addition (+)")
    print("2) Subtraction (-)")
    print("3) Multiplication (*)")
    print("4) Division (/)")

    choice = get_int_choice("Choice: ", 1, 4)

    val_1 = get_number("Please enter your first number: ")
    val_2 = get_number("Please enter your second number: ")

    operations = {
        1: ("+", val_1 + val_2),
        2: ("-", val_1 - val_2),
        3: ("*", round(val_1 * val_2, 1)),
        4: ("/", round(val_1 / val_2, 1))
    }

    op_symbol, correct_answer = operations[choice]

    if choice in (3, 4):
        print("Note: Answer will be rounded to the first decimal place. (e.g. 10.5)")

    guess_prompt = f"What is {val_1} {op_symbol} {val_2}? "
    guess = get_number(guess_prompt)

    if guess == correct_answer:
        print(f"Correct! {val_1} {op_symbol} {val_2} = {correct_answer}\n")
    else:
        print(f"I am sorry but that is incorrect. {val_1} {op_symbol} {val_2} = {correct_answer}\n")
