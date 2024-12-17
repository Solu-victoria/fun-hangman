# Hangman Game 🎮

This is a fun, interactive console-based Hangman game built with Python. It incorporates sound effects using the `pygame` library to enhance the gaming experience. Players try to guess a randomly chosen word, one letter at a time, while keeping their lives intact!

---

## Features

- **Sound Effects:** Correct guesses, wrong guesses, and other game events are accompanied by sound effects.
- **Background Music:** Engaging background music plays throughout the game.
- **Dynamic Gameplay:** The game updates the progress of the guessed word in real time.
- **Replay Option:** Players can choose to replay or exit after a game ends.
- **Word Pool:** Words are loaded dynamically from a file (`HangmanWords.txt`).

---

## Requirements

- Python 3.6 or higher
- `pygame` library

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Solu-victoria/fun-hangman.git
cd fun-hangman
```

### 2. Install Dependencies
Install `pygame`, the library used for sound and music, via `pip`:
```bash
pip install pygame
```

### 3. Ensure Files Are Present
- **Word File:** Make sure `HangmanWords.txt` (containing the word list) is in the project directory.
- **Sound Files:** Ensure all sound files (e.g., `sounds/correct.mp3`, `sounds/wrong.mp3`) are in the `sounds/` folder.
- **Art File:** Ensure the `HangmanArt.py` file is present for displaying the Hangman stages.

---

## How to Play

1. Run the game:
   ```bash
   python HangmanGame.py
   ```
2. The game will:
   - Play a short intro sound and display the welcome screen.
   - Randomly select a word from the `HangmanWords.txt` file for you to guess.
3. Input a single letter at a time.
4. The game provides feedback:
   - Correct guesses reveal letters in the word.
   - Incorrect guesses reduce your lives by 1.
   - You win if you guess all letters before running out of lives.
5. Exit the game anytime by typing `exit`.

---

## Game Controls

- **Guess a Letter:** Input a single letter.
- **Exit Game:** Type `exit` when prompted to guess a letter.
- **Replay Game:** After a game ends, input `y` to replay or `n` to quit.

---

## Game Files Structure

```
Hangman_Game/
├── HangmanArt.py          # Contains ASCII art for Hangman
├── HangmanWords.txt       # Word list for the game
├── sounds/                # Folder containing sound effects
│   ├── correct.mp3
│   ├── wrong.mp3
│   ├── gameover.flac
│   ├── win.mp3
│   ├── try_again.mp3
│   ├── background.mp3
│   └── waiting.mp3
└── hangman.py             # Main Python script
```

---

## Troubleshooting

1. **Pygame Not Installed:**  
   If `pygame` is not found, ensure you've installed it using:
   ```bash
   pip install pygame
   ```

2. **Sound Not Playing:**  
   - Check if the `sounds/` directory exists and contains the required sound files.
   - Ensure your computer's audio is enabled and volume is turned up.

3. **File Not Found Errors:**  
   Verify that `HangmanWords.txt` and `HangmanArt.py` are in the same directory as the main script.

---

### Enjoy the Game! 🎉