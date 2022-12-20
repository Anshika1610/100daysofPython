from replit import clear
from art import logo
def highest_bidder(bidding):
  highest=0
  winner=""
  for bidder in bidding:
    bidamount=bidding[bidder]
    bidamount=int(bidamount)
    if bidamount>highest:
      highest=bidamount
      winner=bidder
  print(f"The winner is {winner} with the bid of ${highest}")
  
  
print(logo)
print("Welcome to the secret auction program.")
bids = {}
name = input("What is your name?: ")
bid = input("What is your bid?: $")
answer = input("Are there any other bidders? Type 'YES' or 'NO'. ")
bids[name] = bid
while answer == 'YES':
    clear()
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bids[name] = bid
    answer = input("Are there any other bidders? Type 'YES' or 'NO'. ")
if answer == 'NO':
    clear()
    highest_bidder(bids)


