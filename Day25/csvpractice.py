#!/usr/bin/python3
"""main to handle csv"""

import csv
import pandas
from functools import reduce


with open("./weather-data.csv", 'r', encoding='utf-8') as my_file:
    reader = csv.reader(my_file)
    data = list(reader)
    temp = [int(i[1]) for i in data[1:]]
    #print(temp)


# Pandas can also be use to read csv file and print it as tabular data
datas = pandas.read_csv("./weather-data.csv")
#print(datas.to_dict('index'))


# You can as well access a single column just like accessing a dictionary

# temps = datas['temp'].to_list()

# total = reduce(lambda x, y: x + y, temps)

# avg = total / len(temps)
# print(avg)
# print(datas['temp'].mean())
# print(datas['temp'].max())

# new = reduce(lambda x, y: x if x < y else y, temps)

# print(new)

#print(datas.Temps)


# Simple queries can as well be carried out
# To find the columns with the maximum temperature


# print(datas[datas.temp == datas.temp.max()])


# print(datas[datas.day == 'Monday'].temp * (9 / 5) + 32)

# You can also create data from scratch．For example

results = {
    'students': ['Amy', 'James', 'Jean'],
    'scores': [70, 83, 92]
}

result_data = pandas.DataFrame(results)

# You can as well save a generated dataframe as a csv file

# result_data.to_csv('./report_card.csv')

squirrel_data = pandas.read_csv('./2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')


count = squirrel_data.groupby(["Primary Fur Color"])['Primary Fur Color'].count()

color_dict = count.to_dict()

new_data = {
    'Fur Color': color_dict.keys(),
    'count': color_dict.values()
}

squirrel_count = pandas.DataFrame(new_data)

squirrel_count.to_csv('./squirrel_count.csv')


#count.to_csv('./squirrel_count.csv')
