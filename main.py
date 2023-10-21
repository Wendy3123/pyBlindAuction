import os
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
bidding_finished = False

def findHighestBidder(bidding_record):
  highest_bid = 0
  winner = ''
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"{winner} has the highest bid of ${highest_bid}")

while not bidding_finished:
  name = input('Whats your name:\n')
  price = int(input('Whats your bid:\n$'))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
  if should_continue == 'no':
    bidding_finished = True
    findHighestBidder(bids)
  elif should_continue == 'yes': 
    os.system('clear')
print(bids)

      

