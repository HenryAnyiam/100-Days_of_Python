#!/usr/bin/python3
"""automatically send mails on birthdays"""

from smtplib import SMTP
import pandas
from random import randint
from datetime import datetime

day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
birthdays = pandas.read_csv("./birthdays.csv")
birthdays = birthdays.to_dict(orient="index")

celebrants = [birthdays[i] for i in birthdays
              if (birthdays[i]["month"] == month) and
              (birthdays[i]["day"] == day)]

with SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="taskhub2023@gmail.com",
                     password="xmyp fkpl evos iltv")
    for i in celebrants:
        letter = randint(1, 3)
        with open(f"./letter_templates/letter_{letter}.txt") as my_letter:
            message = my_letter.read()
            age = year - i["year"]
            message = message.replace("[NAME],",
                                      f"{i['name']},\n\n"
                                      f"A beautiful {age} years\n")
            connection.sendmail(from_addr="taskhub2023@gmail.com",
                                to_addrs=i["email"],
                                msg=f"Subject: Happy Birthday\n\n{message}")
