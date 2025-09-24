# Answer Checker
def answer_checker():
    val_1 = None
    val_2 = None
    ans = None
    guess = None
    choice = None
    
    # Menu:
    print("\nPlease choose the problem type of your choice:")
    print("1) Addition +")
    print("2) Subtraction -")
    print("3) Multiplacation *")
    print("4) Division /")
    
    # Get user choice
    while choice is None:
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # Menu choices:
    # Addition
    if choice == 1:
        # Enter Value 1 and check that it is a number
        while val_1 is None:
            try:
                val_1 = int(input("Please enter your first number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Enter Value 2 and check that it is a number
        while val_2 is None:
            try:
                val_2 = int(input("Please enter your second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Calculate answer
        ans = val_1 + val_2
        
        # Get Guess
        while True:
            try:
                guess = int(input(f"What is {val_1} + {val_2}? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Tell user if answer is correct
        if guess == ans:
            print(f"Correct! {val_1} + {val_2} = {ans}\n")
        else:
            print(f"I am sorry but that is incorrect. {val_1} + {val_2} = {ans}\n")
        
    # Subtraction
    elif choice == 2:
        # Enter Value 1 and check that it is a number
        while val_1 is None:
            try:
                val_1 = int(input("Please enter your first number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Enter Value 2 and check that it is a number
        while val_2 is None:
            try:
                val_2 = int(input("Please enter your second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Calculate answer
        ans = val_1 - val_2
        
        # Get Guess
        while True:
            try:
                guess = int(input(f"What is {val_1} - {val_2}? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Tell user if answer is correct
        if guess == ans:
            print(f"Correct! {val_1} - {val_2} = {ans}\n")
        else:
            print(f"I am sorry but that is incorrect. {val_1} - {val_2} = {ans}\n")
        
    # Multiplacation
    elif choice == 3:
        # Enter Value 1 and check that it is a number
        while val_1 is None:
            try:
                val_1 = int(input("Please enter your first number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Enter Value 2 and check that it is a number
        while val_2 is None:
            try:
                val_2 = int(input("Please enter your second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Convert Int to Float
        fval_1 = float(val_1)
        fval_2 = float(val_2)
        
        # Calculate answer
        ans = fval_1 * fval_2
        ans = round(ans, 1)
        
        # Get Guess
        while True:
            try:
                print("Rounded to the first decimal place. (e.g. 10.5)")
                guess = float(input(f"What is {val_1} * {val_2}? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Tell user if answer is correct
        if guess == ans:
            print(f"Correct! {val_1} * {val_2} = {ans}\n")
        else:
            print(f"I am sorry but that is incorrect. {val_1} * {val_2} = {ans}\n")
        
    # Division
    elif choice == 4:
        # Enter Value 1 and check that it is a number
        while val_1 is None:
            try:
                val_1 = int(input("Please enter your first number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Enter Value 2 and check that it is a number
        while val_2 is None:
            try:
                val_2 = int(input("Please enter your second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Convert Int to Float
        fval_1 = float(val_1)
        fval_2 = float(val_2)
        
        # Calculate answer
        ans = fval_1 / fval_2
        ans = round(ans, 1)
        
        # Get Guess
        while True:
            try:
                print("Rounded to the first decimal place. (e.g. 10.5)")
                guess = float(input(f"What is {val_1} / {val_2}? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        # Tell user if answer is correct
        if guess == ans:
            print(f"Correct! {val_1} / {val_2} = {ans}\n")
        else:
            print(f"I am sorry but that is incorrect. {val_1} / {val_2} = {ans}\n")
    

