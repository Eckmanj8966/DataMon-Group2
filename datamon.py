# 9/13/2025
# 
# Group 2

import answer_checker as ac
import memory_bank as mb

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
        try:
            choice = int(input("Please enter the number of your choice: "))
            print("")
        except ValueError:
            print("Invalid Input. Please enter a valid input: ")
            continue
        
        # Menu choices:
        # Answer Checker
        if choice == 1:
            ac.answer_checker()
        
        # Memory Bank
        elif choice == 2:
            mb.menu()
            
        # Number Guesser
        elif choice == 3:
            print("DEBUG: 3")
            
        # Exit
        elif choice == 4:
            print("DEBUG: 4")
        

if __name__ == "__main__":

    main()




