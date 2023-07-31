""" import csv

with open("c:/Users/João Bettencourt/Documents/GitHub/100DayChallenge/Python/Day23/weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for line in data:
        print(data)
        if line[1] != "temp":
            temperatures.append(int(line[1]))
    print (temperatures)

input("")
 """
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])
input("")