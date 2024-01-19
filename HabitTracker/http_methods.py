#!/usr/bin/python3
"""practice various http methods"""

import requests
from datetime import datetime


# Create a new user
user = {
    "token": "Aa!8vq89VyQ&CLw$+",
    "username": "lexlouis",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url="https://pixe.la/v1/users", json=user)
print(response.text)


# Create a new graph

graph_params = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

graph_header = {
    "X-USER-TOKEN": "Aa!8vq89VyQ&CLw$+"
}


response = requests.post(url="https://pixe.la/v1/users/lexlouis/graphs",
                         headers=graph_header,
                         json=graph_params)
print(response.text)


# Add data to graph

graph_data = {
    "date": datetime(year=2024, month=1, day=18).strftime("%Y%m%d"),
    "quantity": "9.74"
}

response = requests.post(url="https://pixe.la/v1/users/lexlouis/graphs/graph1",
                         headers=graph_header,
                         json=graph_data)
print(response.text)


# Update a pixel
response = requests.put(url="https://pixe.la/v1/users/lexlouis/graphs/graph1/20240118",
                        headers=graph_header,
                        json={"quantity": "18.2"})
print(response.text)

# Delete a pixel
response = requests.delete(url="https://pixe.la/v1/users/lexlouis/graphs/graph1/20240118",
                           headers=graph_header)
print(response.text)
