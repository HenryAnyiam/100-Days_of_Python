#!/usr/bin/python3

import requests


class Post:
    
    def __init__(self) -> None:
        response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.data = response.json()

    def get_blog(self, id):
        for i in self.data:
            if i['id'] == id:
                return i