# Answer Checker
def answer_checker():
    val_1 = None
    val_2 = None
    ans = None
    guess = None
    
    # Menu:
    print("\nPlease choose the problem type of your choice:")
    print("1) Addition +")
    print("2) Subtraction -")
    print("3) Multiplacation *")
    print("4) Division /")
    
    # Get user choice
    choice = int(input("Choice: "))
    
    # Menu choices:
    # Addition
    if choice == 1:
        val_1 = int(input("What is your first number "))
        val_2 = int(input("What is your second number "))
        
        ans = val_1 + val_2
        
        guess = int(input(f"What is {val_1} + {val_2} = "))
        
        if guess == ans:
            print(f"Correct! {val_1} + {val_2} = {ans}\n")
            
        else:
            print(f"I am sorry but that is incorrect. {val_1} + {val_2} = {ans}\n")
        
    # Subtraction
    elif choice == 2:
        val_1 = int(input("What is your first number "))
        val_2 = int(input("What is your second number "))
        
        ans = val_1 - val_2
        
        guess = int(input(f"What is {val_1} - {val_2} = "))
        
        if guess == ans:
            print(f"Correct! {val_1} - {val_2} = {ans}\n")
            
        else:
            print(f"I am sorry but that is incorrect. {val_1} - {val_2} = {ans}\n")
        
    # Multiplacation
    elif choice == 3:
        val_1 = float(input("What is your first number "))
        val_2 = float(input("What is your second number "))
        
        ans = val_1 * val_2
        ans = round(ans, 1)
        
        print("Rounded to the first decimal place. (e.g. 10.5)")
        guess = float(input(f"What is {val_1} * {val_2} = "))
        
        if guess == ans:
            print(f"Correct! {val_1} * {val_2} = {ans}\n")
            
        else:
            print(f"I am sorry but that is incorrect. {val_1} * {val_2} = {ans}\n")
        
    # Division
    elif choice == 4:
        val_1 = float(input("What is your first number "))
        val_2 = float(input("What is your second number "))
        
        ans = val_1 / val_2
        ans = round(ans, 1)
        
        print("Rounded to the first decimal place. (e.g. 10.5)")
        guess = float(input(f"What is {val_1} / {val_2} = "))
        
        if guess == ans:
            print(f"Correct! {val_1} / {val_2} = {ans}\n")
            
        else:
            print(f"I am sorry but that is incorrect. {val_1} / {val_2} = {ans}\n")
    

