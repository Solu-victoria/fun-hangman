# Hangman Game

## Features

### 🎵 **Audio Enhancements**
- Sound effects for correct and incorrect guesses, wins, and game overs.
- **Holiday Special:** A festive soundtrack for the holiday season (Dec 10 - Jan 10).
  
### 📝 **Gameplay Features**
- Difficulty Levels: Choose between Easy, Medium, or Hard.
- Progress Tracker: Updates the guessed word in real-time.
- Replay Option: Play again or exit after completing a game.
- **Leaderboard:** Tracks your game history, including wins, losses, and detailed trial stats.

### 📁 **Dynamic Word Loading**
- Words are loaded from separate files for each difficulty level (`EasyHangmanWords.txt`, `MedHangmanWords.txt`, `HardHangmanWords.txt`).

---

## Requirements

- Python 3.6 or higher
- `pygame` library for sound effects and background music

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Solu-victoria/fun-hangman.git
cd fun-hangman
```

### 2. Install Dependencies
Install `pygame`:
```bash
pip install pygame
```

### 3. Ensure Files Are Present
- **Word Files:** Ensure `EasyHangmanWords.txt`, `MedHangmanWords.txt`, and `HardHangmanWords.txt` are in the `assets/words` directory.
- **Sound Files:** Verify the presence of sound effects (`correct.mp3`, `wrong.mp3`, etc.) in the `assets/music` directory.
- **Art File:** Ensure `HangmanArt.py` is in the `assets` folder.

---

## How to Play

1. Run the game:
   ```bash
   python hangman.py
   ```
2. Pick a difficulty level:
   - `e` for Easy  
   - `m` for Medium  
   - `h` for Hard  
3. Guess the word:
   - Enter a single letter to guess.
   - Type `exit` to leave the game early.
4. Game Feedback:
   - Correct guesses reveal letters in the word.
   - Incorrect guesses reduce lives and display a Hangman stage.
5. Win/Loss:
   - Win by guessing all letters correctly before running out of lives.
   - Lose if your lives reach zero.
6. Replay or Exit:
   - After the game ends, choose to replay (`y`) or exit (`n`).

---

## Game Controls

| **Action**       | **Input**                             |
|-------------------|---------------------------------------|
| Guess a Letter    | Type any single letter               |
| Exit Game         | Type `exit`                         |
| Confirm Exit      | Type `y` (yes) or `n` (no)          |
| Replay Game       | Type `y` (yes) or `n` (no)          |

---

## Leaderboard

The game tracks your performance and displays a detailed leaderboard at the end. Here's what it includes:
- **Summary:**
  - Total games played
  - Number of wins and losses
- **Trial Details:**  
  For each game:
  - Trial number
  - Difficulty level
  - Lives left
  - Number of wrong guesses
  - Outcome (win or loss)
  - Word guessed

---

## Troubleshooting

1. **Missing Word Files:**
   - Ensure the required word files are present in `assets/words`.
   - The game cannot start without these files.

2. **Sound Issues:**
   - Check the `assets/music` folder for sound files.
   - Ensure your system audio is working.

3. **Pygame Errors:**
   - Verify `pygame` installation:
     ```bash
     pip install pygame
     ```

---

## File Structure

```
fun-hangman/
├── assets/
│   ├── music/
│   │   ├── background.mp3
│   │   ├── backgroundChristmas.mp3
│   │   ├── correct.mp3
│   │   ├── gameover.flac
│   │   ├── try_again.mp3
│   │   ├── waiting.mp3
│   │   └── win.mp3
│   ├── words/
│   │   ├── EasyHangmanWords.txt
│   │   ├── MedHangmanWords.txt
│   │   └── HardHangmanWords.txt
│   └── HangmanArt.py
├── LICENSE
├── TODO.md
├── index.py
└── README.md
```
---

## Important Warning ⚠️
Ensure that you are in the **fun-hangman** directory before running the game.  
Running the game from a different directory may result in **File Not Found** or other errors due to missing assets like words, music, or art.

---

## LICENSE
This project is licensed under the MIT License. See the `LICENSE` file for more details.

--- 