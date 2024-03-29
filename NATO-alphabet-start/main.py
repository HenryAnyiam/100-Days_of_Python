#!/usr/bin/python3

import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
  
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv('./nato_phonetic_alphabet.csv')

data_alpha = {row.letter: row.code for index, row in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    try:
        word = input("Enter a word: ").upper()

        result = [data_alpha[i] for i in word]
    except KeyError:
        print("Please input only alphabets")
    else:
        break

print(result)

