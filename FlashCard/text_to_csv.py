#!/usr/bin/python3

import pandas

with open("./file.txt", "r", encoding="utf-8") as my_file:
    data = my_file.readlines()
    data = [i.strip().split() for i in data]
    values = [i[-1] for i in data]
    new_data = pandas.DataFrame({"french_words": values})
    new_data.to_csv("./new_data.csv")
