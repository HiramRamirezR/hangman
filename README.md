# Hangman Game

A classic command-line Hangman game implemented in Python.

## Description

This is a simple yet fun implementation of the classic Hangman word-guessing game. The player tries to guess a secret word, letter by letter, before the hangman is fully drawn. The game randomly selects a word from a predefined list, and the player has a limited number of attempts to guess it correctly.

## How to Play

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd your-repository-name
    ```

3.  **Run the game:**
    ```bash
    python ahorcado.py
    ```
4.  The game will start, and you will be prompted to enter a letter.
5.  Guess the word before you run out of attempts!

## Features

*   Randomly selected words for endless fun.
*   Visual feedback with an ASCII art hangman.
*   Keeps track of remaining attempts.
*   Prevents guessing the same letter multiple times.
*   Clear and simple command-line interface.

## Implementation

The game is written in Python and is contained in a single file, `ahorcado.py`. It uses the `random` library to select a word from a predefined list. The core of the game is a `while` loop that continues as long as the player has attempts remaining. Inside the loop, the game prompts the user for a letter, checks if the letter is in the word, and updates the game state accordingly. The hangman is drawn using a list of strings that represent the different stages of the drawing.

## Contributing

Contributions are welcome! If you have any ideas for improvements or find any bugs, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
