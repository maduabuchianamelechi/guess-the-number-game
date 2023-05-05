#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Import Logo (ASCII object)
from art import logo
import random
# Set Global Scope Variables
HARD_LEVEL = 5
EASY_LEVEL = 10

def choose_dif():
    dif_level = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if dif_level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(user_guess, number, num_attempts):
    """
    - Checks if the user's guess is correct.
    - Returns the numer of user attempts remaining
    """
    if user_guess > number:
        print("Too high.")
        return num_attempts - 1
    elif user_guess < number:
        print("Too low.")
        return num_attempts - 1
    else:
        print(f"You got it! the answer was {number}.")

def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    # Choose a number between 1 and 100
    number = random.randint(1, 100)

    # Set the number of attempts based on the difficulty level
    num_attempts = choose_dif()

    user_guess = 0
    while(user_guess != number):
        # Tell the user the number of attempts remaining
        print(f"You have {num_attempts} attempts remaining to guess the number.")

        # Ask the user to make a guess
        user_guess = int(input("Make a guess: "))

        # Check if the guess is correct and reduce the number of attempts
        num_attempts = check_answer(user_guess, number, num_attempts)
            
        if num_attempts == 0:
            print("You've run out of attempts, you lose.")
            return
        elif user_guess != number:
            print("Guess again.")

game()