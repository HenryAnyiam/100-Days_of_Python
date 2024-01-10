#!/usr/bin/python3
"""manage and save password"""

import json
from random import randint, choice, shuffle


class PasswordManager:
    """save and generate password"""

    _password_file = None
    _user_data = None

    def __init__(self, location: str) -> None:
        type(self)._password_file = location
        self.get_data()

    def get_data(self) -> None:
        """load saved data"""
        try:
            location = type(self)._password_file
            with open(location, 'r', encoding="utf-8") as my_file:
                type(self)._user_data = json.load(my_file)
        except FileNotFoundError:
            type(self)._user_data = {}

    def save_password(self, details: dict) -> None:
        """save password in json format"""
        try:
            location = type(self)._password_file
            data = type(self)._user_data
            with open(location, 'w', encoding='utf-8') as my_file:
                key = details.get("website", "")
                data[key] = details
                json.dump(data, my_file)
        except TypeError:
            pass

    def generate_password(self) -> str:
        """generate a strong random password"""
        letters = [chr(i) for i in range(65, 91)]
        letters.extend([chr(i) for i in range(97, 123)])
        numbers = [str(i) for i in range(10)]
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        nr_letters = randint(8, 10)
        nr_symbols = randint(2, 4)
        nr_numbers = randint(2, 4)
        password_list = [choice(letters) for i in range(nr_letters)]
        password_list.extend([choice(symbols) for i in range(nr_symbols)])
        password_list.extend([choice(numbers) for i in range(nr_numbers)])
        shuffle(password_list)
        password = "".join(password_list)
        return password
