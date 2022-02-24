###Blackjack Project ###
from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_score = 0
computer_score = 0
game_on = True

while game_on:
  if user_score == 21:
    game_on = False
    print(f"your final cards are: {user_cards}. final score: {user_score}")
    print(f"computer's final cards are: {computer_cards}. final score: {computer_score}")
    print(f"You Won by Blackjack😎")
  elif computer_score == 21:
    game_on = False
    print(f"your final cards are: {user_cards}. final score: {user_score}")
    print(f"computer's final cards are: {computer_cards}. final score: {computer_score}")
    print(f"You Lost, computer won by Blackjack😭")
  elif user_score > 21:
    game_on = False
    print(f"your final cards are: {user_cards}. final score: {user_score}")
    print(f"computer's final cards are: {computer_cards}. final score: {computer_score}")
    print(f"You Lost, you went over😬")
  elif computer_score > 21:
    game_on = False
    print(f"your final cards are: {user_cards}. final score: {user_score}")
    print(f"computer's final cards are: {computer_cards}. final score: {computer_score}")
    print(f"You Won, computer went over😏")
  else:
    if input("Do you want to play a game of Blackjack? ('y'|'n')? ") == 'y':
      clear()
      print(logo)
      user_cards = [random.choice(cards),random.choice(cards)]
      user_score = sum(user_cards)
      computer_cards = [random.choice(cards),random.choice(cards)]
      computer_score = sum(computer_cards)
      print(f"your cards are: {user_cards}. current score: {user_score}")
      print(f"computer's first card is: {computer_cards[0]}")
      if input("Type 'y' to get another card, type 'n' to pass:") == 'y':
        user_cards.append(random.choice(cards))
        user_score = sum(user_cards)
      elif computer_score < 18:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
      print(f"your cards are: {user_cards}. current score: {user_score}")
      print(f"computer's first card is: {computer_cards[0]}")