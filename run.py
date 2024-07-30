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

def choose_topic(topics):
    """Prompt the user to choose a topic and select a random word from that topic."""
    while True:
        print("\nChoose a topic:")
        for i, topic in enumerate(topics.keys(), 1):
            print(f"{i}. {topic.capitalize()}")

        user_input = input("\nEnter the number or name of your choice: ").strip().lower()

        if user_input.isdigit():
            choice = int(user_input) - 1
            if 0 <= choice < len(topics):
                selected_topic = list(topics.keys())[choice]
                return selected_topic, random.choice(topics[selected_topic])
            else:
                print("\nInvalid choice. Please enter a number corresponding to a topic.")
        elif user_input in topics:
            selected_topic = user_input
            return selected_topic, random.choice(topics[selected_topic])
        else:
            print("\nInvalid choice. Please enter the number or name of a valid topic.")

def print_hangman(incorrect_guesses):
    """Print the current stage of the hangman based on the number of incorrect guesses."""
    if(incorrect_guesses == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 1):
        print("\n+---+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 2):
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\\ |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\\ |")
        print("/   |")
        print("   ===")
    elif(incorrect_guesses == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\\ |")
        print("/ \\ |")
        print("   ===")

def display_current_state(word, guessed_letters):
    """Display the current state of the word with guessed letters and underscores for unguessed letters."""
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print("Current word: " + " ".join(display))

def handle_guess(word, guessed_letters, incorrect_guesses):
    """Handle the player's guess, update guessed letters and incorrect guesses, and return them."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter.")
        else:
            break
    if guess in word:
        guessed_letters.append(guess)
    else:
        incorrect_guesses.append(guess)
        print_hangman(len(incorrect_guesses))
    return guessed_letters, incorrect_guesses

def check_win(word, guessed_letters):
    """Check if the player has won by guessing all letters in the word."""
    return all(letter in guessed_letters for letter in word)

def check_loss(incorrect_guesses, max_incorrect):
    """Check if the player has lost by exceeding the maximum number of incorrect guesses."""
    return len(incorrect_guesses) >= max_incorrect

# List of topics to choose
TOPICS = {
    "chemistry": [
        "atom", "molecule", "reaction", "acid", "base",
        "catalyst", "electrolyte", "isotope", "polymer", "ion",
        "compound", "element", "solvent", "solute", "precipitate",
        "oxidation", "reduction", "bond", "enzyme", "protein"
    ],
    "geography": [
        "continent", "island", "river", "mountain", "desert",
        "valley", "plateau", "ocean", "volcano", "glacier",
        "delta", "plain", "forest", "savanna", "tundra",
        "climate", "latitude", "longitude", "equator", "meridian"
    ],
    "astronomy": [
        "planet", "star", "galaxy", "nebula", "comet",
        "asteroid", "meteor", "satellite", "orbit", "telescope",
        "quasar", "pulsar", "supernova", "eclipse", "blackhole",
        "constellation", "universe", "cosmos", "moon", "solarsystem"
    ],
    "physics": [
        "force", "energy", "mass", "velocity", "acceleration",
        "momentum", "gravity", "friction", "wave", "particle",
        "quantum", "relativity", "thermodynamics", "magnetism",
        "electricity", "circuit", "radiation", "nucleus", "photon",
        "electron"
    ],
    "mathematics": [
        "algebra", "geometry", "calculus", "equation", "function",
        "matrix", "vector", "probability", "statistics", "theorem",
        "integral", "derivative", "logarithm", "sequence", "series",
        "angle", "triangle", "polygon", "fraction", "decimal"
    ]
}

def main():
    """Main function to run the Hangman game."""
    print_logo()
    player_name = get_player_name()
    print_greeting(player_name)
    print_rules()
    selected_topic, word_to_guess = choose_topic(TOPICS)
    print(f"\nPerfect! You've chosen the topic: {selected_topic}. Let`s start!")

    # Display initial state of the word to guess and the hangman
    guessed_letters = []
    print_hangman(0)
    display_current_state(word_to_guess, guessed_letters)
    
    # Set maximum quantity on incorrect answers
    max_incorrect = 6
    incorrect_guesses = []

    # Enter an infinite loop for handling guesses until the game is won or lost
    while True:
        # Update guessed and incorrect letters based on the player's input
        guessed_letters, incorrect_guesses = handle_guess(
            word_to_guess, guessed_letters, incorrect_guesses
        )
        # Display the current state of the word with guessed letters and underscores
        display_current_state(word_to_guess, guessed_letters)

        # Display the incorrect guesses
        if incorrect_guesses:
            print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")

        # Check if the player has guessed all the letters in the word
        if check_win(word_to_guess, guessed_letters):
            print(f"Congratulations, {player_name}! You've guessed the word: {word_to_guess}")
            break
        # Check if the player has exceeded the maximum number of incorrect guesses
        elif check_loss(incorrect_guesses, max_incorrect):
            print(f"Sorry, {player_name}, you've run out of guesses. The word was: {word_to_guess}")
            break
        
        print(f"Remaining attempts: {max_incorrect - len(incorrect_guesses)}")

if __name__ == "__main__":
    main()