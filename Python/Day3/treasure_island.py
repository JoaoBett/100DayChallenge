print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

direction=input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n--->')

direction=direction.lower()

if direction == ("left"):
    choice=input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swin across.\n")
elif direction == ("right"):
    choice=input("You found a mountain. There is a tunnel hidden between the trees. Type \"go\" if you want to go in. Type \"wait\" to wait for sme miners.\n")
else:
    print("Wrong Path!!\n\n GAME OVER")
    input("")

choice=choice.lower()

if choice == ("wait"):
    choice=input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
elif choice == ("swim"):
    print("You went swimming and died due to the sharks in the lake. \n\n GAME OVER")
elif choice == ("go"):
    choice=input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
else:
    print("Wrong choice!! \n\n GAME OVER")

choice=choice.lower()

if choice == ("red"):
    print("It's a room full of fire.\n\nGAME OVER")
elif choice == ("blue"):
    print("It's a room with a hole that locks you win and start filling water. \n\n GAME OVER")
elif choice == ("yellow"):
    print("It's a room full of gold. \n\n YOU WON!!!")
else:
    print("Wrong choice!\n\n GAME OVER")


input("")