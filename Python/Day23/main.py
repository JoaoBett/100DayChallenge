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
#print(data["temp"])
input("")

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
#print(temp_list)

average = sum(temp_list)/len(temp_list)

data["temp"].mean()

data["temp"].max()

#get data in columns
#print(data["codition"])
data.condition

#get data in row
#print(data[data.day == "Monday"])

#print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32


data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")