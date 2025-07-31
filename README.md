# Hangman Game

A classic command-line Hangman game implemented in Python.

## Description

This is a simple yet fun implementation of the classic Hangman word-guessing game. The player tries to guess a secret word, letter by letter, before the hangman is fully drawn. The game randomly selects a word from an external `words.txt` file, and the player has a limited number of attempts to guess it correctly.

## How to Play

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd your-repository-name
    ```
3.  **(Optional) Customize the words:** You can edit the `words.txt` file to add or remove words. Make sure to keep one word per line.
4.  **Run the game:**
    ```bash
    python ahorcado.py
    ```
5.  The game will start, and you will be prompted to enter a letter.
6.  Guess the word before you run out of attempts!

## Features

*   **Customizable Word Lists:** Easily edit the `words.txt` file to use your own word lists.
*   **Modular Design:** The code is organized into separate modules for game logic and artwork.
*   **Visual Feedback:** Classic ASCII art hangman that is drawn progressively.
*   **Input Validation:** Prevents guessing the same letter multiple times.
*   **Simple Interface:** A clean and straightforward command-line experience.

## Project Structure

The project is organized into the following files:

*   `hangman.py`: The main script containing the core game logic.
*   `ascii_man.py`: A module that stores the ASCII art for the hangman.
*   `words.txt`: A text file containing the list of words for the game.

This structure separates the game's data (words), presentation (art), and logic, making it easier to maintain and expand.

## Contributing

Contributions are welcome! If you have any ideas for improvements or find any bugs, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.