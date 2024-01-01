import os

def add(number1,number2):
    return number1+number2

def subtract(number1,number2):
    return number1-number2
    
def multiply(number1,number2):
    return number1*number2
    
def division(number1,number2):
    return number1/number2

operations = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":division
}    

def calculator():   
    first_number=float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol=input("Pick an operation: ")
        second_number=float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(first_number,second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {result}")

        should_continue=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()
        if should_continue == "n":
            os.system('cls')
            result=0
            should_continue=False
            calculator()
        elif should_continue == "y":
            first_number=result
        elif should_continue == "q":
            break

print("Welcome to the calculator app!\n")
calculator()
print("\nThe calculator app has ended!\n")
input("Press any key to continue...")