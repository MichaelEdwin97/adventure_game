import random
import time

def get_choice():
    while True:
        choice = input("Enter 1 or 2: ")
        if choice in ('1', '2'):
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

def print_description():
    print("Welcome to the Game World!")
    print("You find yourself in a mysterious forest.")
    print("You see two paths ahead.")
    time.sleep(1)

def play_game():
    # Main game loop
    while True:
        print_description()
        print("What will you do?")
        print("1. Take the left path.")
        print("2. Take the right path.")
        
        choice = get_choice()

        if choice == '1':
            print("You chose the left path.")
            # Add the outcome for choice 1 here.
        elif choice == '2':
            print("You chose the right path.")
            # Add the outcome for choice 2 here.
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
