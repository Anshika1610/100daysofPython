import random
from replit import clear
number=random.randint(1,100)
playing=True
while playing:
  print("Welcome to the Guessing Game!\n")
  print("I am thinking of a number between 1 to 100.\n")
  difficulty=input("Choose a level : 'Easy' or 'Hard': ")
  if difficulty=='Easy':
    print("\nYou have 10 attempts to guess the number.\n")
    for i in range(1,11):
      guess=int(input("Make a guess: "))
      if 10-i==0:
        if guess==number:
          print("You have guessed right. You win!")
        elif guess>number:
          print("Too high.")
          print(f"You have {10-i} attempts left.")
          
        elif guess<number:
          print("Too low.")
          print(f"You have {10-i} attempts left.")
          print("You couldn't guess the correct number. You lost.")
              
      elif guess==number:
        print("You have guessed right. You win!")
      elif guess>number:
        print("Too high.")
        print(f"You have {10-i} attempts left.")
        print("Guess again.\n")
      elif guess<number:
        print("Too low.")
        print(f"You have {10-i} attempts left.")
        print("Guess again.\n")
    
  if difficulty=='Hard':
    print("\nYou have 5 attempts to guess the number.\n")
    for i in range(1,6):
      guess=int(input("Make a guess: "))
      if 5-i==0:
        if guess==number:
          print("You have guessed right. You win!")
        elif guess>number:
          print("Too high.")
          print(f"You have {5-i} attempts left.")
          
        elif guess<number:
          print("Too low.")
          print(f"You have {5-i} attempts left.")
          print("You couldn't guess the correct number. You lost.")
        
      elif guess==number:
        print("You have guessed right. You win!")
      elif guess>number:
        print("Too high.")
        print(f"You have {5-i} attempts left.")
        print("Guess again.\n")
      elif guess<number:
        print("Too low.")
        print(f"You have {5-i} attempts left.")
        print("Guess again.\n")
        
  play= input("\nDo you want to continue playing? Type 'Yes to play and 'No to stop. ")
  if play=='No':
    playing=False
  else:
    playing=True
    clear()
  
