print("Welcome to the tip calculator.")

total_bill=float(input("What was the total bill?\n$"))
people_split=int(input("How many people to split the bill?\n"))

bill_person=total_bill/people_split

tip_percentage=int(input("What percentage tip would you like to give?(10%,12'%' or 15%)"))
tip_percentage=tip_percentage/100

final_payment=bill_person+(tip_percentage*bill_person)

print("Each person should pay: " + str(final_payment))

input("Press to continue...")