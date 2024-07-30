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
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(incorrect_guesses == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")


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

print_logo()
player_name = get_player_name()
print_greeting(player_name)
print_rules()
selected_topic, word_to_guess = choose_topic(TOPICS)
print(f"\nPerfect! You've chosen the topic: {selected_topic}. Let`s start!")