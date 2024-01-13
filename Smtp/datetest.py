#!/usr/bin/python3
"""trying the dattime along with the smtplib module"""

from smtplib import SMTP
from datetime import datetime
from random import choice

now = datetime.now()

if now.weekday() == 5:
    quote = ""
    with open("./quotes.txt", 'r', encoding="utf-8") as my_file:
        lines = my_file.readlines()
        quote = choice(lines)
    with SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="taskhub2023@gmail.com",
                         password="xmyp fkpl evos iltv")
        message = f"Subject: Saturday Motivation\n\n{quote}"
        connection.sendmail(from_addr="taskhub2023@gmail.com",
                            to_addrs="louislex95@gmail.com",
                            msg=message)
        