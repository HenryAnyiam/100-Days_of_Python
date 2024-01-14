#!/usr/bin/python3
"""getting the ISS position"""

import requests

response = requests.get(url="https://api.sunrise-sunset.org/json",
                        params={"lat": 6.524379,
                                "lng": 3.379206,
                                "formatted": 0})
print(response.json()) 