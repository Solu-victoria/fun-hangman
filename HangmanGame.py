import random
import HangmanArt
import pygame
import time

pygame.mixer.init()

livesLeft = totalLives = 6

#declaring sound variables
correct = "sounds/correct.mp3"
gameOver = "sounds/gameover.flac"
wrong = "sounds/wrong.mp3"
win = "sounds/win.mp3"
background_music = "sounds/background.mp3"
try_again = "sounds/try_again.mp3"
ready_set_go = "sounds/readySetGo.mp3"
waiting = "sounds/waiting.mp3"
dontLeave = "sounds/nooo.mp3"

# function to play sound
def play_sound(sound_file, vol=0.5, wait=False, message=None):
    sound = pygame.mixer.Sound(sound_file)
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
    pygame.mixer.music.load(music_file)  # Load the background music
    pygame.mixer.music.set_volume(vol)  # Set the volume (0.0 to 1.0)
    pygame.mixer.music.play(loops=-1, start=0.0)  # Play it in a loop

# Function to stop background music
def stop_background_music():
    pygame.mixer.music.stop()  # Stop the background music

# Function to load words from a file
def load_words(filename):
    with open(filename, 'r') as file:
        words = file.readlines()  # Read all lines from the file
    words = [word.strip() for word in words]  # Remove any trailing newline characters
    return words

# function to display hangman
def display_hangman(lives_left):
    print(HangmanArt.HANGMANPICS[totalLives - lives_left])

def handle_guess(userLetterGuess, chosenWordProgress, chosenWord, livesLeft):
    if userLetterGuess not in chosenWord: #letter guessed not in chosen word
        livesLeft -= 1
        play_sound(wrong)
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
    stop_background_music()
    print(f"✨{chosenWord}✨")
    print(HangmanArt.ManFree)
    message = f"Well done! You have correctly guessed the word.\nTHANKS FOR PLAYING!\n"
    play_sound(win, 0.8, True, message)            

def handle_game_over(chosenWord):
    stop_background_music()
    print(HangmanArt.ManDead)
    message = f"**********Sorry you ran out of lives! Thank you for playing. The word was {chosenWord.upper()}.**********\n"
    play_sound(gameOver, 0.8, True, message)

def tryAgain(tryAgainMessage):
    play_sound(try_again)
    print(tryAgainMessage)

def main():
    global livesLeft #to be able to modify the OG livesLeft variable in this main function we used the global keyword

    while True: # as far as the loop has not been broken, then start or restart the game  
        
        # init start
        livesLeft = totalLives # reset lives remaining param
        print("Loading...") # Print loading message while the game is initializing
        time.sleep(2)  # Simulate loading time

        hangmanWords = load_words('HangmanWords.txt') # Load words from the HangmanWords.txt file
        chosenWord = random.choice(hangmanWords)
        chosenWordProgress = list('_' * len(chosenWord))

        stop_background_music()
        play_sound(ready_set_go, 0.8, True)
        # Play background music when the game starts
        play_background_music(background_music, 0.3)
        print(HangmanArt.HangmanIntro)
        #init end

        while livesLeft > 0:
            print(f"\nWord to guess: {''.join(chosenWordProgress)}")
            userLetterGuess = input("Guess a letter or enter 'exit' to leave the game: ").strip().lower()

            if userLetterGuess == 'exit':
                play_sound(dontLeave)
                while True:
                    play_background_music(waiting)
                    confirmExit = input("Are you sure you want to leave the game? Enter 'y' or 'n':\n").strip().lower()
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
                handle_win(chosenWord)
                break 

            display_hangman(livesLeft)
            print(f'*******************YOU HAVE {livesLeft}/{totalLives} LIVES LEFT******************')

        else: #user lost (gameover)
            handle_game_over(chosenWord)

        while True:
            play_background_music(waiting)
            replayGame = input("\nWould you like to play again? Enter 'y' or 'n':\n").strip().lower()
            if replayGame == 'y':
                break
            elif replayGame == 'n':
                return
            else:
                print("Invalid Input. Please enter 'y' or 'n'\n")
        

main()