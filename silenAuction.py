import os
def find_winner(bidder_data):
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
    price = int(input("Enter your bid price: "))
    bidder_data[name] = price
    question = input("Are there more bidder? Type 'yes' to continue and 'no' to quit:  ")
    
    if question == 'no':
        find_winner(bidder_data)
        otherBidder = True
    elif question == 'yes':
        os.system('cls') #to clear the terminal screen

