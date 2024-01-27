#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
content = response.text


soup = BeautifulSoup(markup=content, features="html.parser")

print(soup.prettify())

