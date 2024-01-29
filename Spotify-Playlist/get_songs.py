#!/usr/bin/python3
"""create a spotify playlist from billboard"""

from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


start_date = input("Input year to create playlist from - YYYY: ")
if not start_date:
    raise ValueError("No input received")

try:
    start_date = date(year=int(start_date),
                    month=1, day=1)
except ValueError or TypeError:
    raise ValueError("Incorrect year format")
else:
    if start_date > date.today():
        raise ValueError("Incorrect year. Input a back date")

diff = date.today() - start_date
diff = diff.days
top = 10 if diff >= 100 else (100 // diff)

top_music = set()


artists_class = "li ul li span"
songs_class = "li ul li h3"
while len(top_music) < 100 and start_date < date.today():
    curr_date = str(start_date)
    url = f"https://www.billboard.com/charts/hot-100/{curr_date}"
    response = requests.get(url=url)
    content = response.text
    soup = BeautifulSoup(markup=content, features="html.parser")
    
    songs = soup.select(songs_class)
    artists = soup.select(artists_class)
    i = 0
    j = 0
    number = 10
    while i < number and j < len(artists):
        try:
            int(artists[j].get_text().strip())
        except ValueError:
            if artists[j].get_text().strip() != '-':
                top_music.add((songs[i].get_text().strip(),
                            artists[j].get_text().strip()))
                i += 1
        finally:
            j += 1
    start_date += timedelta(weeks=1)
    if start_date >= date.today():
        start_date -= timedelta(weeks=1)
        number = 100 - len(top_music)

songs = []
artists = []
for i in top_music:
    songs.append(i[0])
    artists.append(i[1])

new_dataframe = DataFrame({
    "Songs": songs,
    "Artists": artists
})

new_dataframe.to_csv("./top_songs.csv")
