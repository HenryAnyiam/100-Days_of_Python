#!/usr/bin/python3
"""accessing random quotes"""

import requests
from customtkinter import CTk, CTkImage, CTkLabel, CTkButton
from PIL import Image


# response = requests.get(url="https://zenquotes.io/api/quotes/")
# print(response.status_code)
# data = response.json()

class Quotes:

    def __init__(self) -> None:
        response = self.get_quotes()
        self.quotes = response.json()
        self.status = response.status_code
        self.get_quotes()

    def get_quotes(self) -> None:
        """get quotes from API"""
        response = requests.get(url="https://zenquotes.io/api/quotes/")
        return response


class QuotesUI(CTk):
    """UI for quotes"""

    def __init__(self) -> None:
        super().__init__()
        self.title("Daily Quotes")
        self.quotes_class = Quotes()
        self.quotes_list = self.quotes_class.quotes
        self.configure(padx=30, pady=30, fg_color="white")
        background = CTkImage(light_image=Image.open("./background.png"),
                              size=(300, 400))
        self.quotes = CTkLabel(self, image=background, text="",
                               font=("Times new Roman", 25, "bold"))
        self.quotes.grid(row=0, column=0, padx=10, pady=10)

        paw = CTkImage(light_image=Image.open("./paw.jpeg"), size=(70,70))
        self.next_quote = CTkButton(self, text="", border_width=1,
                                    fg_color="transparent", image=paw,
                                    width=75, height=75, command=self.load_quote)
        self.next_quote.grid(row=1, column=0, padx=10, pady=10)
        self.load_quote()
    
    def populate_quotes(self) -> None:
        """populates quotes"""
        response = self.quotes_class.get_quotes()
        if response.status_code != 200:
            self.populate_quotes()
        self.quotes_list.extend(response.json())
    
    def load_quote(self) -> None:
        """load quote to UI"""
        if len(self.quotes_list) <= 2:
            self.populate_quotes()
        quote = self.quotes_list.pop(0)
        length = 0
        curr_quote = quote['q'].split()
        message = ""
        hold = ""
        for i in curr_quote:
            message += i + " "
            hold += i + " "
            length += 1
            if (length % 4 == 0) or len(hold) >= 21:
                message += "\n"
                hold = ""
        message += f"...\n\n    {quote['a']}"
        self.quotes.configure(text=message)
        


if __name__ == "__main__":
    app = QuotesUI()
    app.mainloop()
