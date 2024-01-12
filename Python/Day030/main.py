import datetime as dt
import random
import pandas
import smtplib

email = "batata@gmail.com"
password = "abc1234"

now = dt.datetime.now()
today_day = now.day()
today_month = now.month()
today = (today_month, today_day)

data = pandas.read_csv("Day030/birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"Day030/letter_templates/letter{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password) 
        connection.sendmail(from_addr=email,
                             to_addrs=birthdays_person["email"],
                             msg=f"Subject: Happy Birthday's!\n\n{contents}")