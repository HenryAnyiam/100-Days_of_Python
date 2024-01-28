#!/usr/bin/python3
"""scrape a website for top movies"""

import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://web.archive.org/web/20200518073855/"
                        "https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(markup=content, features="html.parser")

movies = soup.select(selector=".title")
movies = [i.get_text() for i in movies]

def checker(val):
    try:
        int(val[0])
    except ValueError:
        return False
    else:
        return True
movies = [i.replace(')', '') for i in movies if checker(i)]

def sorter(val):
    num = 0
    for i in val:
        try:
            hold = int(i)
        except ValueError:
            return num
        else:
            num *= 10
            num += hold
    return num
movies.sort(key=sorter)


with open("movies.txt", 'w', encoding="utf-8") as my_file:
    for i in movies:
        my_file.write(f"{i}\n")