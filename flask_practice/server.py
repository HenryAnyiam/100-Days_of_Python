#usr/bin/python3

from flask import Flask

app = Flask(__name__)


def make_underline(func):
    """decorator to underline"""
    def wrapper(name):
        text = func(name)
        return f"<u>{text}</u>"
    return wrapper


def make_bold(func):
    """decorator to bolden"""
    def wrapper(name):
        text = func(name)
        return f"<b>{text}</b>"
    return wrapper


def make_emphasis(func):
    """emphasize text"""
    def wrapper(name):
        text = func(name)
        return f"<em>{text}</em>"
    return wrapper


@app.route("/<name>", strict_slashes=False)
@make_bold
@make_emphasis
@make_underline
def index(name):
    return f"hello {name}".upper()


if __name__ == "__main__":
    app.run(port=5000, debug=True)