# 9/13/2025
# 
# Joshua Eckman

import datamon_functions as df

def main():
    choice = None
    
    # Menu while loop
    while choice != 4:
        # Display Menu
        print("---------Menu--------")
        print("1) Answer Checker")
        print("2) Memory Bank")
        print("3) Number Guesser")
        print("4) Exit")
        print("---------------------")
        
        # Get user choice
        choice = int(input("Please enter the number of your choice: "))
        
        # Menu choices:
        # Answer Checker
        if choice == 1:
            df.answer_checker()
        
        # Memory Bank
        elif choice == 2:
            print("DEBUG: 2")
            
        # Number Guesser
        elif choice == 3:
            print("DEBUG: 3")
            
        # Exit
        elif choice == 4:
            print("DEBUG: 4")
        

if __name__ == "__main__":
    main()