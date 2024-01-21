#!/usr/bin/python3
"""handle flight search
"""

from os import getenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_handler = DataManager(auth=getenv('AUTH'))

flight_handler = FlightSearch(key=getenv('APIKEY'), flights=data_handler.codes)

updates = data_handler.compare_prices(flights=flight_handler.searched_flights)


if updates:
    notification_handler = NotificationManager(sender="taskhub2023@gmail.com",
                                               receiver="louislex95@gmail.com",
                                               password=getenv('PASSWORD'))
    message = "Subject: Cheap Flights Found\n\n"
    message += "The following flights has been found at better prices\n"
    for i in updates:
        message += f"{i}: {updates[i]}\n"
    message += "\nPlease log on to the website to place bookings"
    notification_handler.send_mail(message=message)
