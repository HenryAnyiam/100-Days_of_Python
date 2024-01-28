#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
content = response.text


soup = BeautifulSoup(markup=content, features="html.parser")


tags = soup.select(selector=".titleline > a")
texts = [i.get_text() for i in tags]
links = [i.get("href") for i in tags]

score = soup.find_all(name='span', class_='score')
scores = [i.get_text() for i in score]
scores = [int(i.split()[0]) for i in scores]

max_vote = max(scores)
index = scores.index(max_vote)

# print(links)
# print(texts)
# print(scores)
print(texts[index])
print(links[index])
print(max_vote)
