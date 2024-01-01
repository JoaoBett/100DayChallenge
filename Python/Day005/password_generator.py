import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['+','-','/','*','~','^','<','>','&','%','@','!','|']

print("Welcome to the PASSWORD GENERATOR\n")
size_ammount=int(input("Choose a size of your password.\n"))
symbols_ammount=int(input("How many symbols would you like?\n"))
numbers_ammount=int(input("How many numbers would you like?\n"))
letters_ammount =size_ammount-(symbols_ammount+numbers_ammount)

password=[]

for symbol in range(symbols_ammount+1):
    password.append(random.choice(symbols))

for number in range(numbers_ammount+1):
    password.append(str(random.choice(numbers)))

for letter in range(letters_ammount+1):
    password.append(random.choice(letters))

random.shuffle(password)

print("Here's your password: " + ''.join(password))
input("\nPress any key to continue...")