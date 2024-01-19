#!/usr/bin/python3
"""monitor the tesla stock trade"""

import requests
from datetime import date, timedelta
from smtplib import SMTP

# Get Stock closing prices between the past two daya
stock_params = {
    "apikey": "IQVQ2TSUD8Y7KFA3",
    "datatype": "json",
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA"
}

yesterday = str(date.today() - timedelta(days=1))
the_day_before = str(date.today() - timedelta(days=2))


data = requests.get(url="https://www.alphavantage.co/query",
                    params=stock_params)
if (data.status_code != 200):
    exit(1)
daily_data = data.json().get('Time Series (Daily)')

if daily_data:
    yday_close = float(daily_data[yesterday]['4. close'])
    day_before_close = float(daily_data[the_day_before]['4. close'])

    percent = round(((yday_close - day_before_close) / yday_close) * 100, 1)
else:
    percent = 1

news_params = {
    "apiKey": "e57585c245da4686a5a7024e7680a6a8",
    'q': "Tesla Inc",
    "from": yesterday,
}

# Get stock news
news_data = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
if (news_data.status_code != 200):
    exit(1)
print(news_data.json())
news = news_data.json()["articles"][0:3]


# send to mail
with SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="taskhub2023@gmail.com", password="xmyp fkpl evos iltv")
    mail = f"Subject: Tesla Inc Stock {'Rises' if percent > 0 else 'Falls'}\n\n"
    mail += f"Tesla Inc: {abs(percent)}% {'Rise' if percent > 0 else 'Fall'}\n\n"
    print(news)
    for i in news:
        mail += f"Headline: {i['title']}\n"
        mail += f"News: {i['url']}\n\n"
    mail = mail.encode(encoding="utf-8")
    connection.sendmail(from_addr="taskhub2023@gmail.com",
                        to_addrs="louislex95@gmail.com",
                        msg=mail)
