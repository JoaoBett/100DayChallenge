import random
import os

def hard_game(number_thought):
    """Starts the hard level game which has 5 lives"""
    lives=5

    while lives != 0:    
        print(f"You have {lives} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if guess == number_thought:
            print(f"You got it! The answer was {number_thought}.\n")
            break
        elif guess > number_thought:
            print("Too high.")
        elif guess < number_thought:
            print("Too low.")
        print("Guess again.\n")
        lives -= 1
    if lives == 0:
        print("You've run out of guesses, you lose...\n")

def easy_game(number_thought):
    """Starts the easy level game which has 10 lives"""
    lives = 10 
        
    while lives != 0:    
        print(f"You have {lives} attempts remaining to guess the number.\n")
        guess=int(input("Make a guess: "))
        if guess == number_thought:
            print(f"You got it! The answer was {number_thought}.")
            break
        elif guess > number_thought:
            print("Too high.")
        elif guess < number_thought:
            print("Too low.\n")
        print("Guess again.\n")
        lives -= 1
    if lives == 0:
        print("You've run out of guesses, you lose")

print("Welcome to the Number Guessing Game!\n")
def play_game():
    end_guessing = False

    while not end_guessing:  
        number_thought = random.randint(1,100)
        print("I am thinking in a number between 1 and 100.\n")
        difficulty=input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()

        if difficulty == "easy":
            easy_game(number_thought)
        elif difficulty == "hard":
            hard_game(number_thought)
        else:
            print("Wrong Spelled")
        
        should_continue=input("Do you want to play again? Type 'y' to yes, type 'n' to no.\n").lower()

        if should_continue != "y":
            os.system("cls")
            print("The program has ended.")
            input("Press any key to continue...")
            end_guessing = True
        else:
            os.system("cls")

play_game()