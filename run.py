import random

def get_player_name():
    """Prompt the user for their name and validate the input."""
    while True:
        player_name = input("Enter your name: ").strip()
        if player_name.isalpha():
            return player_name
        else:
            print("Invalid input. Please enter a valid name (letters only).")

def print_greeting(player_name):
    """Print the greeting message and game introduction."""
    print(f"Welcome to Hangman, {player_name}!")
    print("This classic word guessing game will test your vocabulary and spelling skills.")
    print("Try to guess the hidden word one letter at a time.")
    print("If you can guess the word before running out of guesses, you win!")
    print("Good luck and have fun!\n")

player_name = get_player_name()
print_greeting(player_name)