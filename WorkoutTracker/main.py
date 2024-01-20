#!/usr/bin/python3
"""track workout"""

import requests
from os import getenv
from datetime import datetime

exercise = input("tell me what exercises did you do today?: ")
if exercise:
    header = {
        'Content-Type': "application/json",
        "x-app-id": getenv("APPID"),
        "x-app-key": getenv("APPKEY")
    }
    body = {
        "query": exercise
    }
    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                             headers=header,
                             json=body)
    if response.status_code == 200:
        data = response.json()["exercises"]
        for i in data:
            today = datetime.now()
            body = {
                "workout": {
                    "date": today.strftime("%d/%m/%Y"),
                    "time": today.strftime("%H:%M:%S"),
                    "exercise": i['name'].title(),
                    "duration": i["duration_min"],
                    "calories": i["nf_calories"]
                }
            }
            header = {
                "Authorization": f"Bearer {getenv('AUTH')}"
            }
            response = requests.post(url="https://api.sheety.co/fc899fc681b980ccca8049dea1cfcd63/myWorkouts/workouts",
                                     headers=header,
                                     json=body)
            print(response.text)
            print(response.status_code)

    else:
        print(response.text)
else:
    print("No exercise inputed")
