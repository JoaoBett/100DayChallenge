import random
import os
from game_data import data

def get_data():
    """Gets random data for each option"""
    account = random.choice(data)
    return account

def format_data(account):
    """Format the data and make it printable"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def compare(a_followers, b_followers, correct_guess):
    """Checks if the user_guess was right"""
    if a_followers > b_followers:
        return correct_guess == "a"
    else:
        return correct_guess == "b"

print("Welcome to the Higher or Lower game.")
def play_game():
    end_game = False
    score = 0
    user_guess = ""
    a = get_data()
    b = get_data()

    while a == b:
        b= get_data()

    while not end_game:
        format_data(a)
        format_data(b)
        is_correct=compare(a["follower_count"],b["follower_count"],user_guess)

        print(f"Compare A: {format_data(a)}.") 
        print("VS")
        print(f"Against B: {format_data(b)}.") 

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = a["follower_count"]
        b_follower_count = b["follower_count"]
        
        is_correct=compare(a_follower_count,b_follower_count,user_guess)
        os.system("clear")
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            a=b
            b=get_data()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            
            should_continue = input("Do you want to play again? Type 'y' for yes, type 'n' for no.").lower()
            if should_continue != "y":
                print("The game has ended.")
                input("Press any key to continue...")
                end_game = True
            else:
                os.system("cls")



play_game()