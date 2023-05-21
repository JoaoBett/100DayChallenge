import random

user_choice=int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS.\n"))
print("You choose:")
if user_choice == 0:
    print("\nROCK\n")
elif user_choice == 1:
    print("\nPAPER\n")
elif user_choice == 2:
    print("\nSCISSORS\n")

print("Computer chose:")
computer_choice=random.randint(0,2)

if computer_choice == 0:
    print("\nROCK\n")
elif computer_choice == 1:
    print("\nPAPER\n")
elif computer_choice == 2:
    print("\nSCISSORS\n")
else:
    print("Wrong Choice\n")


if user_choice == 0 and computer_choice == 0:
    print("--->DRAW")
elif user_choice == 0 and computer_choice == 1:
    print("--->COMPUTER WINS")
elif user_choice == 0 and computer_choice == 2:
    print("--->YOU WIN\n")

if user_choice == 1 and computer_choice == 0:
    print("--->YOU WIN")
elif user_choice == 1 and computer_choice == 1:
    print("--->DRAW")
elif user_choice == 1 and computer_choice == 2:
    print("--->COMPUTER WINS\n")

if user_choice == 2 and computer_choice == 0:
    print("--->COMPUTER WINS")
elif user_choice == 2 and computer_choice == 1:
    print("--->YOU WIN")
elif user_choice == 2 and computer_choice == 2:
    print("--->DRAW\n")


input("\nPress any key to exit...")