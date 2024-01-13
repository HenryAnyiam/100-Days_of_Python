#!/usr/bin/python3
"""populate birthday csv"""

import pandas


names = ["Mum", "Dad", "Jessie"]
email = ["louislex95@gmail.com",
         "louislex95@gmail.com",
         "louislex95@gmail.com"
         ]
year = [1975, 1969, 2003]
month = [1, 1, 11]
day = [13, 13, 13]
data = {
    "name": names,
    "email": email,
    "year": year,
    "month": month,
    "day": day
}

dataframe = pandas.DataFrame(data)
dataframe.to_csv("./birthdays.csv", index=False)
