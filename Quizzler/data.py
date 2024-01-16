#!/usr/bin/python3
"""get questions from API"""

import requests


parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 12
}

data = requests.get(url="https://opentdb.com/api.php", params=parameters)

data = data.json()

question_data = data["results"]
