import random
import assets.HangmanArt as HangmanArt
import pygame
import time
from datetime import datetime

pygame.mixer.init()

totalLives = 6
wrongGuesses = list()
leaderboard = {
    'no_of_games' : 0,
    'no_of_losses' : 0,
    'no_of_wins' : 0,
    'trials_details' : []
}

def is_holiday_season():
    today = datetime.today()
    year = today.year

    # Define holiday season range
    holiday_start = datetime(year - 1, 12, 10) if today.month == 1 else datetime(year, 12, 10)
    holiday_end = datetime(year, 1, 10) if today.month == 1 else datetime(year + 1, 1, 10)

    # Check if today falls within the holiday season range
    return holiday_start <= today <= holiday_end

#declaring sound variables
correct = "correct.mp3"
gameOver = "gameover.flac"
wrong = "wrong.mp3"
win = "win.mp3"
background_music = "backgroundChristmas.mp3" if is_holiday_season() else "background.mp3"
try_again = "try_again.mp3"
ready_set_go = "readySetGo.mp3"
waiting = "waiting.mp3"
dontLeave = "nooo.mp3"

# function to play sound
def play_sound(sound_file, vol=0.5, wait=False, message=None):
    sound = pygame.mixer.Sound("assets/music/"+sound_file)
    pygame.mixer.stop()  # Stop any currently playing sounds
    sound.set_volume(vol)  # Set volume (0.0 to 1.0)
    sound.play()

    if message:
        print(message)

    if wait:  # If waiting is required
        while pygame.mixer.get_busy():  # Check if the mixer is still playing
            pygame.time.wait(100)  # Pause the game for 100ms to allow playback

# Function to play background music
def play_background_music(music_file, vol=0.5):
    pygame.mixer.music.load("assets/music/"+music_file)  # Load the background music
    pygame.mixer.music.set_volume(vol)  # Set the volume (0.0 to 1.0)
    pygame.mixer.music.play(loops=-1, start=0.0)  # Play it in a loop

# Function to stop background music
def stop_background_music():
    pygame.mixer.music.stop()  # Stop the background music

# Function to load words from a file
def load_words(filename):
    with open("assets/words/"+filename, 'r') as file:
        words = file.readlines()  # Read all lines from the file
    words = [word.strip() for word in words]  # Remove trailing newline characters
    return words

# function to display hangman
def display_hangman(lives_left):
    print(HangmanArt.HANGMANPICS[totalLives - lives_left])

def handle_guess(userLetterGuess, chosenWordProgress, chosenWord, livesLeft):
    if userLetterGuess not in chosenWord: #letter guessed not in chosen word
        livesLeft -= 1
        play_sound(wrong)
        wrongGuesses.append(userLetterGuess)
        print(f"Wrong! You guessed {userLetterGuess}, that's not in the word. You lose a life.")
        

    else: #if letter guessed is in chosen word   
        # replacing '_' with userLetterGuess in chosenWordProgress
        for index, letter in enumerate(chosenWord):
            if letter == userLetterGuess:
                chosenWordProgress[index] = userLetterGuess  # Replace the correct dash with the guessed letter
        
        play_sound(correct)
        print(f"\nCorrect! {''.join(chosenWordProgress)}")
    return chosenWordProgress, livesLeft

def handle_win(chosenWord):
    leaderboard['no_of_wins'] +=1
    stop_background_music()
    print(f"✨{chosenWord}✨")
    print(HangmanArt.ManFree)
    message = f"Well done! You have correctly guessed the word.\nTHANKS FOR PLAYING!\n"
    play_sound(win, 0.8, True, message)
    return 'You won'            

def handle_game_over(chosenWord):
    stop_background_music()
    print(HangmanArt.ManDead)
    message = f"**********Sorry you ran out of lives! Thank you for playing. The word was {chosenWord.upper()}.**********\n"
    play_sound(gameOver, 0.8, True, message)
    return 'You lost'

def tryAgain(tryAgainMessage):
    play_sound(try_again)
    print(tryAgainMessage)

def displayLeaderboard():
    leaderboard['no_of_losses'] = leaderboard['no_of_games'] - leaderboard['no_of_wins']
    print("\n************** LEADERBOARD **************\n")
    
    # Display Summary
    print("+--------------+-------------+---------------+")
    print("| No. of Games | No. of Wins | No. of Losses |")
    print("+--------------+-------------+---------------+")
    print(f"|      {leaderboard['no_of_games']}       |      {leaderboard['no_of_wins']}      |      {leaderboard['no_of_losses']}        |")
    print("+--------------+-------------+---------------+\n")

    # Display Trial Details
    print("Details of Trials:")
    print("+---------+------------------+----------+------------+-------------------+---------------+")
    print("| Trial # | Difficulty Level |   Word   | Lives Left | Wrong Guesses No. | Judgement     |")
    print("+---------+------------------+----------+------------+-------------------+---------------+")
    for trial in leaderboard['trials_details']:
        print(f"|    {trial['trialNo']}    |    {trial['difficultyLevel']:>13} |{trial['word']:>13}|     {trial['livesLeft']}      |         {trial['wrongGuessesNo']}         | {trial['judgement']:>13} |")
    print("+---------+------------------+------------+------------+-------------------+---------------+\n")

def main():
    try:
        while True: # as far as the loop has not been broken, then start or restart the game  
            
            # INIT START
            livesLeft = totalLives # reset lives remaining param
            wrongGuesses.clear()
            print("\nLoading...") # Print loading message while the game is initializing
            time.sleep(2)  # Simulate loading time
            
            play_background_music(waiting)
            while True:
                difficultyLevel = input("\nPick a difficulty level. Enter 'e' for easy, 'm' for medium or 'h' for hard: ").strip().lower()
                if difficultyLevel == 'e':
                    wordsFile = 'EasyHangmanWords.txt'
                    break
                elif difficultyLevel == 'm':
                    wordsFile = 'MedHangmanWords.txt'
                    break
                elif difficultyLevel == 'h':
                    wordsFile = 'HardHangmanWords.txt'
                    break
                else:
                    print("Invalid Input. Please enter 'e' for easy, 'm' for medium or 'h' for hard")
                    continue

            hangmanWords = load_words(wordsFile) # Load words from the words file
            chosenWord = random.choice(hangmanWords)
            chosenWordProgress = list('_' * len(chosenWord))

            print("\nLoading...") # Print loading message while the game is initializing
            time.sleep(2)  # Simulate loading time
            stop_background_music()

            play_sound(ready_set_go, 0.8, True)
            # Play background music when the game starts
            play_background_music(background_music, 0.3)
            print(HangmanArt.HangmanIntro)
            leaderboard['no_of_games'] +=1
            #INIT END

            while livesLeft > 0:
                if difficultyLevel == 'e' and wrongGuesses:
                    print(f"\nYou have guessed these wrong: {', '.join(wrongGuesses)}")

                print(f"\nWord to guess: {''.join(chosenWordProgress)}")
                userLetterGuess = input("Guess a letter or enter 'exit' to leave the game: ").strip().lower()

                if userLetterGuess == 'exit':
                    play_sound(dontLeave)
                    while True:
                        play_background_music(waiting)
                        confirmExit = input("Are you sure you want to leave the game? Your player history would be lost. Enter 'y' or 'n':\n").strip().lower()
                        if confirmExit != 'n' and confirmExit != 'y':
                            print("Invalid Input. Please enter 'y' or 'n'\n")
                            continue
                        break
                    if confirmExit == 'y':
                        play_sound(dontLeave,vol=0.8,wait=True)
                        return #leave game
                    else:
                        play_background_music(background_music, 0.3)
                        continue    
                elif not userLetterGuess.isalpha() or len(userLetterGuess) != 1: #validating input
                    tryAgain("Invalid input. Your guess must be a single letter")
                    continue
                elif userLetterGuess in chosenWordProgress: #already guessed the letter
                    tryAgain(f"You have already guessed {userLetterGuess}")
                    continue

                #check if player's guess is correct or wrong and return the new progress and livesLeft
                chosenWordProgress, livesLeft = handle_guess(userLetterGuess, chosenWordProgress, chosenWord, livesLeft)

                if '_' not in chosenWordProgress: #user has successfully guessed the word (win)
                    judgement = handle_win(chosenWord)
                    break 

                display_hangman(livesLeft)
                print(f'*******************YOU HAVE {livesLeft}/{totalLives} LIVES LEFT******************')

            else: #user lost (gameover)
                judgement = handle_game_over(chosenWord)
            
            #end of game trial
            trialDeets = { # dictionary of information for this particular game trial
                'trialNo' : leaderboard['no_of_games'],
                'difficultyLevel' : difficultyLevel,
                'livesLeft' : livesLeft,
                'wrongGuessesNo' : len(wrongGuesses),
                'judgement' : judgement,
                'word' : chosenWord
            }
            leaderboard['trials_details'].append(trialDeets)

            while True:
                play_background_music(waiting)
                replayGame = input("\nWould you like to play again? Enter 'y' or 'n':\n").strip().lower()
                if replayGame == 'y':
                    break # leave this loop and replay general loop
                elif replayGame == 'n':
                    play_sound(dontLeave,vol=0.8,wait=True)
                    return #leave game
                else:
                    print("Invalid Input. Please enter 'y' or 'n'\n")
    except FileNotFoundError:
        print("Something went wrong, words file not found.")  
        print("The game cannot proceed without the words file. Exiting...")

main()
displayLeaderboard()