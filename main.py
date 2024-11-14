from art import logo 

print(logo)
bids = {} 
continue_bidding = False 

# bidding_record = {"Angela": 123, "James": 321}
def find_highest_bidder(bidding_record):
    highest_bidder = 0 
    winner = ""
    
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount 
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")


while not continue_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price 
    should_continues = input("Are there any other bidders? Type 'yes' or 'no'. \n " )
    if should_continues == 'no': 
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continues == 'yes':
        should_continues 
    

        
    

