#!/usr/bin/python3

from flask import Flask, render_template, url_for
from datetime import date
import requests


app = Flask(__name__)

def get_data(name):
    age_res = requests.get("https://api.agify.io/",
                           params={"name":name})
    gender_res = requests.get("https://api.genderize.io/",
                              params={"name": name})
    age = age_res.json().get("age")
    gender = gender_res.json().get("gender")
    return age, gender


@app.route("/", strict_slashes=False)
def index():
    return render_template("index1.html", year=date.today().year)

@app.route("/guess/<name>", strict_slashes=False)
def guess(name):
    data = get_data(name)
    return render_template("guess.html",
                           name=name.title(),
                           age=data[0],
                           gender=data[1])


if __name__ == "__main__":
    app.run(port=5000, debug=True)