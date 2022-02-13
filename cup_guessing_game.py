from random import shuffle
import time

# variable setup
cups = ['X','X','X']
guess = ''
correct_cup = -1

# let the user place the ball under cup 1, 2, or 3
# verify that input and place ball
def user_places_ball():
    place_ball = ''
    while place_ball not in ['1','2','3']:
        place_ball = input("First, place this ball... O ... under cup 1, 2 or 3: ")
    position = int(place_ball) - 1
    cups[position] = 'O'

# shuffle the cups and record where the ball is shuffled to
def shuffle_cups(cups, correct_cup):
    print("Now watch as I shuffle the cups!! Don't lose track of the ball!!")

    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('.')
    time.sleep(1.5)
    print('.')

    shuffle(cups)
    correct_cup = cups.index('O')
    return correct_cup

# let the user guess but verify that their guess is 1, 2, or 3
def user_guess(guess):
    while guess not in ['1','2','3']:
        guess = input("YOU HAVE ONE GUESS!! IS THE BALL UNDER CUP 1, 2, OR 3? ")
    guess = int(guess) - 1
    return guess

# see if they are right, and if not, tell them where the ball was
def check_guess(guess, correct_cup):
    if guess == correct_cup:
        guess += 1
        print(f"YOU WIN!!! THE BALL WAS UNDER CUP #{guess}")
    else:
        correct_cup += 1
        print(f"YOU LOSE!!! THE BALL WAS UNDER CUP #{correct_cup}")


# Main game logic
# 1. User places a ball
# 2. We shuffle the cups and learn the new ball position
# 3. User makes a guess
# 4. We check that guess
print("WELCOME TO THE BALL GUESSING GAME!!")
user_places_ball()
print("Take a close look at the cups: " + str(cups))
time.sleep(2)
correct_cup = shuffle_cups(cups, correct_cup)
guess = user_guess(guess)
check_guess(guess, correct_cup)