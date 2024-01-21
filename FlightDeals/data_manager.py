#!/usr/bin/python3
"""Data Manager Module"""

import requests
from typing import List, Dict


class DataManager:
    """Handle syncing with google sheets"""

    def __init__(self, auth: str) -> None:
        """initialize DataMangaer Class"""
        self.__header = {
            "Authorization": f"Bearer {auth}"
        }
        self.__data = self.get_data()
        self.__f_data = {i['iataCode']: i for i in self.__data}
        self.codes = [i['iataCode'] for i in self.__data]

    def get_data(self) -> List[Dict]:
        """get data from google sheets"""
        response = requests.get(url="https://api.sheety.co/"
                                "fc899fc681b980ccca8049dea1cfcd63"
                                "/flightDeals/prices",
                                headers=self.__header)
        return response.json()['prices']

    def compare_prices(self, flights: Dict = {}) -> None:
        """compare prices and update if need be"""
        self.updated = {}
        for i in flights:
            data = self.__f_data[i]
            if flights[i] < data['lowestPrice']:
                self.update_price(data['id'], flights[i])
                self.updated[data['city']] = flights[i]
        return self.updated

    def update_price(self, id: int, price: int) -> None:
        """update price according to id"""
        body = {
            'price': {
                'lowestPrice': price
            }
        }
        requests.put(url="https://api.sheety.co/"
                         "fc899fc681b980ccca8049dea1cfcd63"
                         f"/flightDeals/prices/{id}",
                         json=body,
                         headers=self.__header)
