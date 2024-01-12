#!/usr/bin/python3
"""handle app data"""

import pandas
from random import choice
from typing import Dict, Tuple


class CardData:
    """handle card data"""

    def __init__(self) -> None:
        self.language_data = self.load_data()
        self.data_keys = list(self.language_data.keys())
        self.current_word = choice(self.data_keys)

    def load_data(self) -> Dict:
        """load data to instance"""
        data = pandas.read_csv("./data/fr-en.csv")
        french = data.french_words.to_list()
        english = data.english_words.to_list()
        new_data = {i: (french[i], english[i]) for i in range(1, len(french))}
        return new_data

    def next_data(self, add_back: bool = False) -> Tuple:
        """return another word"""
        if not add_back:
            self.data_keys.remove(self.current_word)
        self.current_word = choice(self.data_keys)
        return self.language_data[self.current_word]
