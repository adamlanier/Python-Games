'''
This script plays the game War.
'''

import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
    'Ace',
)
values = {
    'Two':2,
    'Three':3,
    'Four':4,
    'Five':5,
    'Six':6,
    'Seven':7,
    'Eight':8,
    'Nine':9,
    'Ten':10,
    'Jack':11,
    'Queen':12,
    'King':13,
    'Ace':14,
}


class Card():
    '''
    A simple card from a standard 52 card deck
    '''

    def __init__(self,suit,rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit


class Deck():
    '''
    A collection of 52 unique Cards
    '''

    def __init__(self) -> None:
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle_cards(self) -> None:
        '''
        Shuffles cards in place
        '''
        print("\nShuffling the deck...\n")
        random.shuffle(self.all_cards)

    def deal_one_card(self) -> Card:
        '''
        Returns one card
        '''
        return self.all_cards.pop()

class Player():
    '''
    Includes player hands, methods to modify the hand, and other hand methods
    '''

    def __init__(self,name) -> None:
        self.name = name
        self.all_cards = []

    def remove_one(self):
        '''
        Takes a card from the Player's hand
        '''
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        '''
        Adds cards to the Player's hand. Supports lists or single Card objects
        '''
        if isinstance(new_cards,list):
            # list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # single card object
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        if len(self.all_cards) == 1:
            return f"Player {self.name} has {len(self.all_cards)} card."

        return f"Player {self.name} has {len(self.all_cards)} cards."



# Game Lost function
def you_lost(loser,winner):
    '''
    Message to the loser.
    '''
    print(f"You lost, {loser}. {winner} just defeated you at War.")
    print(f"This game lasted {ROUND_NUMBER} turns.")

# What has been pulled
def on_the_table():
    '''
    Shows what has been pulled by each player for that turn.
    Uncomment these sleeps to make the game more readable.
    Comment these sleeps to make the game play faster.
    '''
    time.sleep(.5)
    print(f"{player_one.name} has pulled the {player_one_cip[-1]}!")
    time.sleep(.5)
    print(f"{player_two.name} has pulled the {player_two_cip[-1]}!")
    time.sleep(.5)


# GAME LOGIC
#
# Create the players

player_one = Player(input("Please enter player one's name: "))
player_two = Player(input("Please enter player two's name: "))

# Create the deck, shuffle it
main_deck = Deck()
main_deck.shuffle_cards()

# Deal the cards out
time.sleep(2)
for x in range(26):
    player_one.add_cards(main_deck.deal_one_card())
    player_two.add_cards(main_deck.deal_one_card())
print(player_one)
print(player_two)
print('')


# Main game loop
ROUND_NUMBER = 0
GAME_ON = True

while GAME_ON:

    # Increase round number, print it to keep track
    ROUND_NUMBER += 1
    print(f"It is now round {ROUND_NUMBER}")

    if ROUND_NUMBER % 10 == 0:
        # This will pause every 10 rounds. Useful when simulating fast games. 
        print("\nWhew, let's take a break...")
        time.sleep(2)
        print(player_one)
        print(player_two)
        print('')
        time.sleep(1)

    # Check to see if we have a loss
    if len(player_one.all_cards) == 0:
        you_lost(player_one.name,player_two.name)
        break
    if len(player_two.all_cards) == 0:
        you_lost(player_two.name,player_one.name)
        break

    # Start a new round with cards in play
    player_one_cip = []
    player_one_cip.append(player_one.remove_one())

    player_two_cip = []
    player_two_cip.append(player_two.remove_one())

    # Card comparison
    while True:

        # Let them know who pulled what
        on_the_table()


        if player_one_cip[-1].value > player_two_cip[-1].value:
            player_one.add_cards(player_two_cip)
            player_one.add_cards(player_one_cip)
            print(f"{player_one.name} wins this round.\n")
            #time.sleep(.5)
            break
        if player_one_cip[-1].value < player_two_cip[-1].value:
            player_two.add_cards(player_one_cip)
            player_two.add_cards(player_two_cip)
            print(f"{player_two.name} wins this round.\n")
            #time.sleep(.5)
            break

        print("IT IS WAR!!!!\n")
        #time.sleep(.5)

        if len(player_one.all_cards) < 20:
            print(f"{player_one.name} doesn't have enough cards for war...")
            you_lost(player_one.name,player_two.name)
            GAME_ON = False
            break
        if len(player_two.all_cards) < 20:
            print(f"{player_two.name} doesn't have enough cards for war...")
            you_lost(player_two.name,player_one.name)
            GAME_ON = False
            break

        for num in range(5):
            player_one_cip.append(player_one.remove_one())
            player_two_cip.append(player_two.remove_one())
        continue

print('')
