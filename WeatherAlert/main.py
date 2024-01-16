#!/usr/bin/python3
"""Open Weather API use"""

import requests
from os import getenv
from twilio.rest import Client

api_key = getenv("API_KEY")
acct_sid = getenv("SID")
auth_token = getenv("AUTH")
phone = getenv("PHONE")
phone2 = getenv("PHONE2")

client = Client(username=acct_sid, password=auth_token)
params = {
    "lat": 6.510590,
    "lon": 3.314030,
    "appid": api_key
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                    params=params)
next_12_hr_dt = data.json()['list'][:4]
weather = [True if i['weather'][0]['id'] < 700 else False for i in next_12_hr_dt]


if True in weather:
    message = "Gurl you better hold a facking umbrella🌂"
else:
    message = "Its a fine weather today hani, Slay!!!💅"

sms = client.messages.create(to=phone2,
                             from_=phone,
                             body=message)
print(sms.status)
