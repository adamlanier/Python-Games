import time

# initial setup
# define empty rows, player names, turn count, win check
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

player_x = 'X'
player_o = 'O'
turn_count = 1
win = False
tie = False
current_index = 0
current_sign = 'X'
valid_placement = [1,2,3,4,5,6,7,8,9]

# function that prints the board
def print_board(r1,r2,r3):
    print("\n")
    print("  " + r1[0] + "  |  " + r1[1] + "  |  " + r1[2] + "  ")
    print("-----+-----+-----")
    print("  " + r2[0] + "  |  " + r2[1] + "  |  " + r2[2] + "  ")
    print("-----+-----+-----")
    print("  " + r3[0] + "  |  " + r3[1] + "  |  " + r3[2] + "  ")
    print("\n")

# function that gets the players input and validates the input
def get_input(player,sign,valid_placement):
    player_input = ''
    valid = False

    while valid == False:
        player_input = input(f"{player}, where would you like to place your {sign}? ")
        if player_input.isdigit() == False:
            print("Please enter a number...")
            continue
        player_input = int(player_input)
        if player_input < 1 or player_input > 9:
            print("Please enter a number between 1-9...")
            continue
        elif player_input not in valid_placement:
            print(f"Sorry, that spot has already been taken! Please place your {sign} in an open spot...")
            continue
        else:
            return player_input

# function to see if the most recent input caused the player to win
def check_win(r1,r2,r3):

    # vertical win
    for num in 0,1,2:
        if r1[num] == r2[num] == r3[num] and r1[num] != " ":
            return True
    
    # horizontal win
    for row in r1,r2,r3:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # diagonal win
    if r1[0] == r2[1] == r3[2] and r1[0] != " ":
        return True
    elif r1[2] == r2[1] == r3[0] and r1[2] != " ":
        return True
    

def close_out_win(winner,loser,turn_count):
    print("WE HAVE A WINNER!!!!")
    print(f"Congratulations, {winner}!! You beat {loser}, and it only took you {turn_count - 1} turns!!")
    play_again()

def close_out_tie(p1,p2):
    print("The game was a tie...zzzz")
    play_again()


# update: adding prompt to ask to play again
def play_again():
    valid_answer = False

    while not valid_answer:
        go_agane = input("Would you like to play again? ").upper()
        if go_agane in ('Y', 'YES', 'YA', 'YEP'):
            valid_answer = True
            print("Here is where you could play again... could")
            # have to clear the board, reset the joinks
            break
        elif go_agane in ('N', 'NO', 'NAH', 'NOPE'):
            valid_answer = True
            print("Thank you for playing :)")
            time.sleep(1)
            break
        else:
            valid_answer = False
            print("Please enter Yes or No.")
            continue
    return

# GAME LOGIC
# Prints the basic intro, gets the player names
print("Welcome to Tic-Tac-Toe!\n")
player_x = input("Please enter the name of the player using the Xs: ")
player_o = input("Please enter the name of the player using the Os: ")
print(f"\n{player_x} VERSUS {player_o} ... GET READY FOR THE BATTLE OF THE CENTURY!!")

# Prints the initial board
time.sleep(2)
print("\nHere is the battle field:")
print_board(row1,row2,row3)

# Only play the game if no one has won, and max turns have not been reached
while win != True and turn_count < 10:
    
    # see whos turn it is,
    if turn_count%2 != 0:
        current_index = get_input(player_x,'X',valid_placement)
        valid_placement.remove(current_index)
        current_sign = 'X'
    else:
        current_index = get_input(player_o,'O',valid_placement)
        valid_placement.remove(current_index)
        current_sign = 'O'

    # place the current sign into the right spot
    if current_index in [1,2,3]:
        row1[current_index - 1] = current_sign
    elif current_index in [4,5,6]:
        row2[current_index - 4] = current_sign
    else:
        row3[current_index - 7] = current_sign

    # increment the turn, print the board, see if the game continues
    turn_count += 1
    print_board(row1,row2,row3)
    if turn_count >= 6:
        win = check_win(row1,row2,row3)
    
    # someone won, congratulate them
    if win:
        if current_sign == 'X':
            close_out_win(player_x, player_o, turn_count)
        else:
            close_out_win(player_o, player_x, turn_count)

if turn_count == 10 and win != True:
    close_out_tie(player_x,player_o)