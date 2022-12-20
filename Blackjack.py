import random
from art import logo
print(logo)

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)
def compare(user_score, computer_score):
  if user_score==computer_score:
    return "Draw"
  elif computer_score==0:
    return "You lose, Opponent has a BlackJack."
  elif user_score==0:
    return "You win."
  elif user_score>21:
    return "You lose, You went over the score."
  elif computer_score>21:
    return "You win, Opponent's score is more than 21."
  elif user_score>computer_score:
    return "You win."
  else:
    return "You lose."
  

is_game_over=False 
user_cards = []
computer_cards = []
for _ in range (2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
while not is_game_over:
  user_score=calculate_score(user_cards)
  computer_score=calculate_score(computer_cards)
  print(f"Your cards are {user_cards} and your score is {user_score}")
  print(f"Computer's first card is {computer_cards[0]}")
  if user_score==0 or user_score>21 or computer_score>21:
    is_game_over=True
  else:
    answer=input("Do you want to draw another card? type 'Yes' to draw and 'No' to stop. ")
    if answer=='No':
      is_game_over=True
    elif answer=='Yes':
        user_cards.append(deal_card())
while computer_score<17 and computer_score!=0:
  computer_cards.append(deal_card())
  computer_score=calculate_score(computer_cards)


print(f"\nYour final cards are {user_cards} and your final score is {user_score}.")
print(f"The computer's final cards are {computer_cards} and its final score is {computer_score}.")
print("\n")
print(compare(user_score,computer_score))

   
