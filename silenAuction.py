import os
import time
def find_winner(bidder_data):
    if not bidder_data:
        print("No bids were placed!!")
        return
    maxBid = 0
    winner = ""
    for bidder in bidder_data:
        if bidder_data[bidder] > maxBid:
            maxBid = bidder_data[bidder]
            winner = bidder
    
    print("Here's the details of all the bidders: ",bidder_data)
    print(f"The winner of the auction is: {winner} with a bid price of: {maxBid}")


bidder_data = {}
otherBidder = False
print("__________Welcome to the Auction Program________")
while not otherBidder:
    name = input("Enter your name: ")
    if not name:
        print("Name cannot be empty!! Try again")
        continue
    if name in bidder_data:
        print(f"Warning! The name {name} is already present! Overwriting the previous bid")
    try:
        price = int(input("Enter your bid price: "))
        if price < 0:
            print("The bid price must be non-negative")
            continue
    except ValueError:
        print("The value of price must be an integer")
        
    bidder_data[name] = price
    question = input("Are there more bidder? Type 'yes' to continue and 'no' to quit: ").strip().lower()
    
    if question == 'no':
        find_winner(bidder_data)
        otherBidder = True
    elif question == 'yes':
        os.system('cls') #to clear the terminal screen
    else:
        print("Invalid input!! Please type 'yes' or 'no'. Considering it a 'yes' by default")
        time.sleep(2)
        os.system('cls')

