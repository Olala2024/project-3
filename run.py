import random

def print_logo():
    logo = """
 _    _                                             
| |  | |                                            
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __      
|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\     
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    
|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|    
                     __/ |                          
                    |___/                           
    """
    print(logo)

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
    print(f"\nWelcome to Hangman, {player_name}!")
    print("This classic word guessing game will test your vocabulary and spelling skills.")
    print("Try to guess the hidden word one letter at a time.")
    print("If you can guess the word before running out of guesses, you win!")
    print("Good luck and have fun!\n")

def print_rules():
    """Print the rules of the game."""
    print("Rules:")
    print("1. Choose a topic from the given list.")
    print("2. Try to guess the hidden word by entering one letter at a time.")
    print("3. You can make up to 6 incorrect guesses.")
    print("4. If you guess all the letters correctly within the limit, you win!")
    print("5. If you exceed 6 incorrect guesses, you lose.")
    print("6. Letters are case-insensitive (e.g., 'A' is the same as 'a').\n")

print_logo()
player_name = get_player_name()
print_greeting(player_name)
print_rules()