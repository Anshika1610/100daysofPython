from art import logo
print(logo)
from game_data import data
import random
from art import vs
from replit import clear

score=0
game_should_continue=True
second_choice=random.choice(data)

while game_should_continue:
  def format_data(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, a {description}, from {country}."
  
  def check(guess,first_followers,second_followers):
    if first_followers>second_followers:
      return guess=='A'
    else:
      return guess=='B'
    
    
  
  first_choice=second_choice
  second_choice=random.choice(data)
  if first_choice==second_choice:
    second_choice=random.choice(data)
  
  first_followers=format_data(first_choice)
  second_followers=format_data(second_choice)
  
  first_followers=first_choice["follower_count"]
  second_followers=second_choice["follower_count"]
  
  
  print(f"Compare A: {format_data(first_choice)}")
  
  print(vs)
  
  print(f"Against B: {format_data(second_choice)}")
  
  guess=input("\nWho has more followers: A or B? ").upper()
  
  is_correct=check(guess,first_followers,second_followers)
  
  if is_correct:
    score+=1
    clear()
    print(logo)
    print(f"You're right! Your score is {score}.")
  else:
    clear()
    print(logo)
    print(f"Sorry, you are wrong. Your final score is {score}.")
    game_should_continue=False
