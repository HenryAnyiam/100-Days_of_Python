#!/usr/bin/python3
"""Module for Question Class"""


class Question:
    """Class to hold question objects"""

    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer

    def __str__(self) -> str:
        return f"[{type(self).__name__}]: {self.text} {self.answer}"
