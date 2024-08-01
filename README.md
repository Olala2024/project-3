# HANGMAN GAME

![responsive image](assets/images/main.png)

## Table of contents

1. [UI](#ui)
2. [Features](#features)
3. [Features Left to Implement](#left)
4. [Technology Used](#tech)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Content](#content)
10. [Acknowledgements](#acknowledgements)

## Project Description

This project is a text-based Hangman game that allows users to guess letters to uncover a hidden word. The game includes multiple topics, each with a list of words, providing a fun and educational experience.

## UI

![Flowchart](assets/images/flowchart.png)

## Features

#### Welcome Screen
The user is greeted with a welcome screen featuring the game's logo. They are prompted to enter their name and confirm their choice.
![welcome page](assets/images/welcome.png)

### Validation

#### Player Name Input

The `get_player_name()` function prompts the user to enter their name and ensures the input meets specific criteria:

1. **Length Check**: The function restricts the name to a maximum of 45 characters to prevent excessively long names. If the input exceeds this limit, the user is notified to provide a shorter name.

2. **Character Check**: The function verifies that the input consists solely of alphabetic characters. This ensures that the name contains only letters, preventing invalid entries that include numbers or special characters.

3. **Input Prompt**: If the input fails either validation check, the user is given a clear and informative error message to guide them in providing valid input.

![validation](assets/images/validation.png)

#### Greeting and Rules

1. **Greeting Message**:
   The `print_greeting(player_name)` function delivers a warm welcome to the player by addressing them by name. It provides an overview of the game’s objectives, explaining that the game is a word guessing challenge designed to test vocabulary and spelling skills. This function aims to create an engaging and informative introduction, ensuring the player understands the game's purpose and how to play.

2. **Game Rules**:
   The `print_rules()` function outlines the rules of the game in a clear and structured manner:
   - The player must choose a topic from a list.
   - They will guess the hidden word one letter at a time.
   - The player is allowed up to 6 incorrect guesses.
   - The game ends with a win if all letters are guessed correctly within the allowed attempts.
   - The game ends with a loss if the number of incorrect guesses exceeds 6.
   - Letter guessing is case-insensitive, meaning 'A' and 'a' are considered the same.

   This section ensures that players are well-informed about the game mechanics before they start playing.

3. **Topic Selection**:
   The `choose_topic(topics)` function allows the player to select a topic from a list. It handles both numeric and textual inputs:
   - The function displays a list of available topics with corresponding numbers.
   - The player can choose a topic by entering the number or name.


   This ensures a smooth and user-friendly topic selection process, contributing to an overall enjoyable gaming experience.

   ![rules](assets/images/rules.png)

    - The function validates the input and selects a random word from the chosen topic.
    - It provides feedback if the input is invalid, prompting the player to make a correct selection.

    