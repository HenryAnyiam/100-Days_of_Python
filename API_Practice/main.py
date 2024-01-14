#!/usr/bin/python3
"""check iss"""

import requests
from datetime import datetime
from smtplib import SMTP
from time import sleep

MY_LAT = 6.510590 # Your latitude
MY_LONG = 3.314030 # Your longitude

iss_latitude = 0
iss_latitude = 0

def get_iss_data():
    global iss_latitude, iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])



#Your position is within +5 or -5 degrees of the ISS position.
def iss_is_close():
    if (((MY_LAT + 5) >= iss_latitude >= (MY_LAT - 5)) and
        ((MY_LONG + 5) >= iss_longitude >= (MY_LONG - 5))):
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


sunrise = 0
sunset = 0
time_now = 0
def get_time_data():
    global sunrise, sunset, time_now
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

def it_is_dark():
    """check if past sunset and before sunrise"""
    if ((time_now.hour >= sunset) or
        (time_now.hour <= sunrise)):
        return True
    return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if iss_is_close() and it_is_dark():
        with SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="taskhub2023@gmail.com",
                             password="xmyp fkpl evos iltv")
            connection.sendmail(from_addr="taskhub2023",
                                to_addrs="louislex95@gmail.com",
                                msg="Subject: ISS\n\nLook Up, ISS is close")
            print("Email Sent")
    sleep(60)
    get_iss_data()
    get_time_data()
