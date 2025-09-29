# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 12:33:30 2025

@author: williamm3560
"""

# Number Guesser
import random

def classic_mode():
    print("\n🎯 Classic Mode")
    secret = random.randint(1, 50)
    attempts = 0
    guess = None

    while guess != secret:
        try:
            guess = int(input("Enter your guess (1-50): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts += 1
        if guess < secret:
            print("🔎 The secret number is HIGHER than", guess)
        elif guess > secret:
            print("🔎 The secret number is LOWER than", guess)
        else:
            print(f"✅ Correct! The secret number was {secret}.")
            print(f"🎉 You solved it in {attempts} tries!")

def range_mode():
    print("\n📏 Range Mode")
    try:
        low = int(input("Enter the lowest number in range: "))
        high = int(input("Enter the highest number in range: "))
    except ValueError:
        print("⚠️ Invalid input. Returning to menu.")
        return

    if low >= high:
        print("⚠️ Invalid range. Returning to menu.")
        return

    secret = random.randint(low, high)
    attempts = 0
    guess = None

    while guess != secret:
        try:
            guess = int(input(f"Enter your guess ({low}-{high}): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts += 1
        if guess < secret:
            print("🔎 The secret number is HIGHER than", guess)
        elif guess > secret:
            print("🔎 The secret number is LOWER than", guess)
        else:
            print(f"✅ Correct! The secret number was {secret}.")
            print(f"🎉 You solved it in {attempts} tries!")

def reflection_mode():
    print("\n🧩 Reflection Mode")
    secret = random.randint(1, 50)
    attempts = 0
    guess = None

    while guess != secret:
        try:
            guess = int(input("Enter your guess (1-50): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts += 1
        if guess < secret:
            print("🔎 The secret number is HIGHER than", guess)
        elif guess > secret:
            print("🔎 The secret number is LOWER than", guess)
        else:
            print(f"✅ Correct! The secret number was {secret}.")
            print(f"🎉 You solved it in {attempts} tries!")

    # Reflection part
    print("\n🧠 Reflection:")
    print("- You didn’t just guess randomly, you used logic.")
    print("- Each hint narrowed the possible range of numbers.")
    print("- Problem-solving means using feedback to reach answers.")
    print("- This is the same method computers use to search & optimize.")

def menu():
    while True:
        print("\n=== Number Guesser Menu ===")
        print("1. Classic Mode")
        print("2. Range Mode")
        print("3. Reflection Mode")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            classic_mode()
        elif choice == "2":
            range_mode()
        elif choice == "3":
            reflection_mode()
        elif choice == "4":
            print("👋 Thanks for playing Number Guesser! Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1-4.")

# Run the game
menu()
