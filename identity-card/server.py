#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)