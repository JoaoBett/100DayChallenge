print("Welcome to the secret auction program!\n")

bid_dictionary = {}
end_auction = False

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not end_auction:
    name=input("What is your name?: ")
    price=int(input("What's your bid?: $"))
    bid_dictionary[name] = price

    option=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if option == "no":
        find_highest_bid(bid_dictionary)
        end_auction = True
    elif option == "yes":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

input("")