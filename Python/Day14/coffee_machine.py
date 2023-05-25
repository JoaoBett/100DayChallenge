MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": { 
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources={
    "water":300,
    "coffee":100,
    "milk":200,
}
profit=0
machine_power = True

QUARTER=0.25
DIME=0.10
NICKEL=0.05
PENNIE=0.01

def amount_money():
    """Calculates the amount of money was inserted on the machine"""
    quarters=int(input("How many quarters? "))
    dimes=int(input("How many dimes? "))
    nickels=int(input("How many nickels? "))
    pennies=int(input("How many pennies? "))

    amount_coins = quarters*QUARTER + dimes*DIME + nickels*NICKEL + pennies*PENNIE
    return amount_coins

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.\n")
            return False
    return True

def coffee_change(coffee_choice, coffee_cost):
    inserted_coins = amount_money()
    change_coins = inserted_coins - coffee_cost

    if change_coins < 0:
        print(f"Sorry, not enough money. Money refunded: ${inserted_coins:.2f}")
    elif change_coins == 0:
        print("You provided the exact amount. Thank you!")
        return True
    else:
        global profit
        profit += coffee_cost
        print(f"Here is your {coffee_choice}. Enjoy!")
        print(f"Here is your change: ${change_coins:.2f}")
        return True

def coffee_making(coffee_choice):
    if coffee_choice in MENU:
        order_ingredients = MENU[coffee_choice]["ingredients"]
        if is_resources_sufficient(order_ingredients):
            for item in order_ingredients:
                resources[item] -= order_ingredients[item]
            return True
        else:
            return False
    else:
        print("Invalid coffee choice.")
        return False

while machine_power:
    coffee_choice = input("What would you like? (espresso, latte, cappuccino): ")
    
    if coffee_choice == "off":
        print("Powering off...")
        input("")
        machine_power = False
    elif coffee_choice == "report":
        """Shows the current resources inside the machine"""
        print("Water: " + str(resources["water"] + "ml"))
        print("Milk: " + str(resources["milk"] + "ml"))
        print("Coffee: " + str(resources["coffee"] + "g"))
        print("Money: " + str(profit) + "$")
    else:
        if coffee_choice in MENU:
            coffee_cost = MENU[coffee_choice]["cost"]
            if coffee_making(coffee_choice):
                coffee_change(coffee_choice, coffee_cost)