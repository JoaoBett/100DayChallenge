import csv
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = len(data[data["Primary Fur Color" == "Black"]])
red = len(data[data["Primary Fur Color" == "Cinnamon"]])
gray = len(data[data["Primary Fur Color" == "Gray"]])


data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray,red,black]
}

df = pd.DataFrame(data_dict)
df.to_csv("new_data.csv")