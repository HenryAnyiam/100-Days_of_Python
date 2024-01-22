#!/usr/bin/python3
"""allow user signup"""

from os import getenv
import requests


class User:
    """handle user sign up"""

    AUTH = getenv("AUTH")

    def __init__(self, **kwargs) -> None:
        """Initialize a new user"""
        values = [
            kwargs.get("first_name"),
            kwargs.get("last_name"),
            kwargs.get("last_name")
        ]
        if None not in values:
            self.first_name = values[0]
            self.last_name = values[1]
            self.email = values[2]
        else:
            self.email = ""
            self.create_user()
        self.save_user()
    
    def create_user(self) -> None:
        """create a new user"""
        self.first_name = input("Please input your first name: ").title()
        self.last_name = input("Please input your last name: ").title()
        email = input("Please input your email: ")
        if email == input("Please verify your email: "):
            self.email = email
        else:
            print("Incorrect email")

    def save_user(self):
        """save user to sheets"""
        auth = type(self).AUTH
        header = {
            "Authorization": f"Bearer {auth}"
        }
        if self.email:
            body = {
                "user": {
                    "firstName": self.first_name,
                    "lastName": self.last_name,
                    "email": self.email
                }
            }
            requests.post(url="https://api.sheety.co"
                          "/fc899fc681b980ccca8049dea1cfcd63"
                          "/flightDeals/users",
                          json=body,
                          headers=header)
    
    @classmethod
    def get_users(cls):
        """get all registered users"""
        header = {
            "Authorization": f"Bearer {cls.AUTH}"
        }
        response = requests.get(url="https://api.sheety.co"
                                "/fc899fc681b980ccca8049dea1cfcd63/"
                                "flightDeals/users",
                                headers=header)
        users = response.json()['users']
        emails = [i['email'] for i in users]
        return emails


if __name__ == "__main__":
    new_user = User()
