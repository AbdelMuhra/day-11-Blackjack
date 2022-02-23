############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = {}
if input("Do you want to play a game of Blackjack? ('y'|'n')? ") == 'y':
  clear()
  print(logo)
  user_cards = [random.choice(cards),random.choice(cards)]
  user_score = sum(user_cards)
  computer_cards = [random.choice(cards),random.choice(cards)]
  computer_score = sum(computer_cards)
  print(f"your cards are: {user_cards}. current score: {user_score}")
  print(f"computer's first card is: {computer_cards[0]}")
