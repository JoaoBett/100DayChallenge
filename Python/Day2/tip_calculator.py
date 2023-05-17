print("Welcome to the tip calculator.")

initial_bill=float(input("What was the total bill?\n-->$"))
tip_percentage=int(input("What percentage tip would you like to give?(10%,12% or 15%)\n-->"))
people_split=int(input("How many people to split the bill?\n-->"))

tip_percentage=tip_percentage/100

tip_ammount=initial_bill*tip_percentage

final_bill=round((initial_bill+tip_ammount)/people_split, 2)

print("Each person should pay: " + str(final_bill))

input("Press to continue...")