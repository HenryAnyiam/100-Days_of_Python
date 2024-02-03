#!/usr/bin/python3
"""simple flask app"""

from flask import Flask, render_template
from random import randint


app = Flask(__name__)


number = randint(0, 9)


@app.route("/", strict_slashes=False)
def index():
    return render_template("index.html")

@app.route("/<int:guess>", strict_slashes=False)
def guess(guess):
    text = "You Found Me"
    color = "Green"
    url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    if guess < number:
        text = "Too Low, Try Again"
        color = "Red"
        url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    elif guess > number:
        text = "Too High, Try Again"
        color = "Purple"
        url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    return render_template("guess.html",
                           text=text,
                           color=color,
                           url=url)


if __name__ == "__main__":
    app.run(port=5000)