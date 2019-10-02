#import our modules
import random
import time
from msvcrt import getwch
from sys import exit

#together this is every card in a full 52 deck excluding jokers
suits = ["Hearts","Spades", "Clubs", "Diamonds"]
types = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

#loop that concatenates the two lists together to create a full list
#far shorter than putting 52 items in one single list
full_deck = []
for s in suits:
    for t in types:
        full_deck.append(f"{t} of {s}")

#does the player know how to play?
require_rules = input('Hello, welcome to Egyptian Python. Press enter to continue, or type "Rules" to be taught the rules. ')
if require_rules == "Rules":
    input('''Every card in your deck or the computer's deck will be shown in the terminal.
If two of the same cards are shown in a row, press the enter button.
If two of the same cards are shown but separated by a single card, press the enter button.
Neither include suits.
If you press enter when not applicable, you lose one card in your deck.
If you are too late to press the enter button, the computer take all the cards shown in the terminal.
If you press the enter button, you take all the cards shown in the terminal.
The first person to gain all the cards is the winner.''')

#class to disable keyboard input
class keyboardDisable:
	def __init__(self):
		self.disable = False
	
	def start(self):
		self.disable = True
	
	def stop(self):
		self.disable = False
		
	def __call__(self):
		while self.disable:
			getwch()
		
disable_keyboard = keyboardDisable()

#shuffle/split the deck

print("Please wait, shuffling deck. ")
disable_keyboard.start()
time.sleep(random.randint(1, 5))
random.shuffle(full_deck)

print("Done shuffling. Splitting deck. This may take some time. ")
time.sleep(random.randint(5, 15))
player_deck = full_deck[:26]
computer_deck = full_deck[:-26]
print("Done shuffling and splitting.")

disable_keyboard.stop

#adjust computer difficulty/reaction time
while True:
    difficulty = input("How hard should the computer be? Type Easy, Medium, or Hard.\n")

    try:
        if difficulty == "Easy":
            comp_speed = random.randint(2,4)
            break
        elif difficulty == "Medium":
            comp_speed = random.randint(1,3)
            break
        elif difficulty == "Hard":
            comp_speed = random.randint(1,2)
            break
    except:
        pass

#gets confirmation from the user if they wish to play
while True:
    user_confirmation = input(f'To confirm, your chosen difficulty is {difficulty}, is that correct? \nType "Yes" to continue. You will either play first or second. ')
    if user_confirmation == "Yes":
        break
    else:
        continue

#countdown loop
for i in reversed(range(6)):
    print(f"Starting game in {i}")
    i += 1
    time.sleep(1)

#decides who plays first
player_turn = random.randint(0, 1)

#now the actual game!
while len(player_deck) > 0 and len(computer_deck) > 0:
    pass
