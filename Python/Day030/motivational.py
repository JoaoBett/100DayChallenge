import datetime as dt
import random
import smtplib

email = "abc@gmail.com"
password = "abc1234"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("Day030/quotes.txt") as data:
        quotes = data.readlines()
        today_quote = random.choice(quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                 to_addrs=email,
                                 msg=f"Subject: Monday\n\n{today_quote}")