#!/usr/bin/python3

import requests

header = {
    "apikey": "uRABzSYoi844D5qm2-54jWrCEy4Xhqo2",
    "Content-Type": "applications/json"
}

params = {
    "fly_from": "LHR",
    "fly_to": "airport:DUS",
    "date_from": "03/04/2024",
    "date_to": "17/04/2024",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "GBP"
}

response = requests.get(url="https://api.tequila.kiwi.com/v2/search",
                        headers=header,
                        params=params)
print(response.status_code)
print(response.json()["data"][0]["price"])

response = requests.get(url="https://api.sheety.co/fc899fc681b980ccca8049dea1cfcd63/flightDeals/prices")
print(response.json())