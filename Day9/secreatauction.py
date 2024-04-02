import os
from art import logo

print("Welcome to the secret auction program.")
print(logo)

replay = 'yes'

aution_dist = {}

bid_value = 0

while replay == 'yes':
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    aution_dist[name] = bid
    replay = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    os.system('cls')

highest_bid = {}

for user, bidding in aution_dist.items():
    if bidding > bid_value:
        highest_bid = {user: bidding}
        bid_value = bidding
    else:
        pass


print(
    f"The winner is {list(highest_bid.keys())[0]} with a bid of ${list(highest_bid.values())[0]}")
