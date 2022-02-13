# Guessing Game Challenge
"""
Let's use `while` loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2. On a player's first turn, if their guess is
 * within 10 of the number, return "WARM!"
 * further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is 
 * closer to the number than the previous guess return "WARMER!"
 * farther from the number than the previous guess, return "COLDER!"
4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!
"""
from hashlib import new
from random import randint

# generate the number the user is looking for
correct_number = randint(1,101)

# setup the list to hold user guesses, guess counter
guesses = [0]
guess_counter = 0

# print the instructions for the user
print("\nWelcome to the Guessing Game!\nTry to find the secret number in the least amount of guesses!\n")

# main game logic
while guesses[-1] != correct_number:
    # validate that they enter an integer
    try:
        # store the user guess, verify that it is between 1-100
        new_guess = int(input("Enter your best guess between 1-100: "))
        if new_guess < 1 or new_guess > 100:
            print("OUT OF BOUNDS. TRY AGAIN.")
            continue
    except ValueError:
        print("You must enter a whole number")
        continue

    # verify that it's a unique guess
    if new_guess in guesses:
        print(f"You have already guessed {new_guess}! Please try again!")
        continue

    # add the guess to the guess list, then increment the counter
    guesses.append(new_guess)
    guess_counter += 1

    # first check if they are correct
    if new_guess == correct_number:
        print(f"YOU WIN!! {new_guess} was the correct number!")
        print(f"It took you {guess_counter} guesses to win the game!")
    
    # if it's their first guess, check to see if they were within 10 of the correct number
    elif guess_counter == 1:
        if abs(new_guess - correct_number) <= 10:
            print("WARM!")
        else:
            print("COLD!")
    
    # if it's guess #2 or more, check if the newest guess is closer than the last guess
    else:
        if abs(new_guess - correct_number) < abs(guesses[-2] - correct_number):
            print("WARMER!")
        elif abs(new_guess - correct_number) == abs(guesses[-2] - correct_number):
            print("JUST AS CLOSE AS YOUR LAST GUESS!!")
        else:
            print("COLDER!")