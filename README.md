# Hangman Game

Welcome to the Hangman game! This is a simple implementation of the classic word-guessing game using Python.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Contributing](#contributing)

## Introduction

Hangman is a word-guessing game where the goal is to guess the word before you run out of attempts. Each incorrect guess results in a part of the hangman being drawn.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/hangman-game.git
    cd hangman-game
    ```

2. **Ensure you have Python installed:**

    This game requires Python 3.x. You can download it from [python.org](https://www.python.org/).

3. **Install the required modules:**

    There are no external dependencies required for this project.

## How to Play

1. **Run the Game:**

    To start the game, simply run the Python script:

    ```bash
    python hangman.py
    ```

2. **Gameplay:**

    - The game will print the logo and the initial state of the word with underscores representing the hidden letters.
    - Players take turns to guess a letter.
    - If the guessed letter is in the chosen word, it will be revealed in the correct positions.
    - If the guessed letter is not in the word, the player loses a life and part of the hangman is drawn.
    - The game continues until the player either wins by guessing all letters correctly or loses all lives.

3. **Winning and Losing:**

    - If you guess all the letters in the word correctly before running out of lives, you win.
    - If you lose all your lives before guessing the word, you lose.

## Features

- Simple and easy-to-understand code.
- Random word selection from a predefined list.
- Visual representation of the hangman stages.
- Text-based interface.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---

**Note:** This project uses artwork and words from the `hangman_art` and `hangman_words` modules which are assumed to be part of the same repository or provided by you. Ensure that these modules are included in your project directory.
