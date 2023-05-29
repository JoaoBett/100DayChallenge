from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_working = True
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

while machine_working:
    options = menu.get_items()
    coffee_choice=input("What would you like? (espresso, latte, cappuccino): ").lower()

    if coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_choice == "off":
        print("Powering off")
        machine_working = False
    else:
        drink = menu.find_drink(coffee_choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)