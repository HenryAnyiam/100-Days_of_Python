#!/usr/bin/python3
"""Flight Search Module"""

from typing import List, Dict
import requests


class FlightSearch:
    """search for flight data"""

    def __init__(self, key: str,
                 city: str = "LON",
                 flights: List[str] = [],
                 dates: List[str] = ["03/04/2024",
                                     "17/04/2024"]) -> None:
        """Initialize FlightSearch Module"""
        self.flights = flights
        self.city = city
        self.dates = dates
        self.__header = {
            "apikey": key,
            "Content-Type": "applications/json"
        }
        self.searched_flights = {}
        self.search_flights()

    def search_flights(self):
        """search cheapest flights"""
        for i in self.flights:
            params = {
                "fly_from": f"city:{self.city}",
                "fly_to": f"airport:{i}",
                "date_from": self.dates[0],
                "date_to": self.dates[1],
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "GBP"
            }
            response = requests.get(url="https://api.tequila.kiwi.com"
                                    "/v2/search",
                                    headers=self.__header,
                                    params=params)
            if response.status_code == 200:
                self.searched_flights[i] = response.json()["data"][0]["price"]
