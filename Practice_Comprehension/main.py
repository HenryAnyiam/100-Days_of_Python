#!/usr/bin/python3

from random import randint
import pandas

name = "Angela"

new = [ord(i) for i in name if i != 'A']

print(new)

names = ["Dave", "Beth", "Caroline", "Alex", "Eleanor", "Freddie" ]

new_names = [i.upper() for i in names if len(i) >= 5]

print(new_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [(i ** 2) for i in numbers]

result = [i for i in numbers if i % 2 == 0]

print(squared_numbers)

print(result)

with open('./file.txt', 'r', encoding='utf-8') as my_file:
    data = my_file.readlines()

with open('./file1.txt', 'r', encoding='utf-8') as my_file:
    data1 = my_file.readlines()

result = [int(i.strip()) for i in data1 if i in data]

result2 = list(set(data).intersection(set(data1)))

print(result)

print(result2)

scores = {name:randint(1, 100) for name in names}

print(scores)

passed_students = {key:value for key, value in scores.items() if value >= 60}

print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split(' ')

result = {word:len(word) for word in sentence_list}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day: round((temp * (9/5) + 32), 1) for day, temp in weather_c.items()}

print(weather_f)

new_data = pandas.DataFrame({'Day': weather_c.keys(),
                             'Temp_C': weather_c.values(),
                             'Temp_F': weather_f.values()})

print(new_data)
# print(new_data[0])
for (index, row) in new_data.iterrows():
    print(index, row)
