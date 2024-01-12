#!/usr/bin/python3
"""create flashcard app ui"""

from customtkinter import CTk, CTkImage, CTkLabel, CTkButton
from PIL import Image
from carddata import CardData


class FlashCardUI(CTk):
    """class to handle app UI"""

    def __init__(self) -> None:
        super().__init__()
        self.title("FlashCard")
        self.configure(fg_color="#B1DDC6", padx=30, pady=30)
        self.data = CardData()
        self.current_data = None
        front = Image.open("./images/card_front.png")
        self.card_front = CTkImage(light_image=front,
                                   size=(550, 400))
        back = Image.open("./images/card_back.png")
        self.card_back = CTkImage(light_image=back,
                                  size=(550, 400))
        self.check = CTkImage(light_image=Image.open("./images/right.png"),
                              size=(70, 70))
        self.cross = CTkImage(light_image=Image.open("./images/wrong.png"),
                              size=(70, 70))

        self.show_french = CTkLabel(self, image=self.card_front, text="",
                                    font=("Times New Roman", 30))
        self.show_french.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.show_english = CTkLabel(self, image=self.card_back, text="",
                                     font=("Times New Roman", 30),
                                     text_color="white")

        self.mark_wrong = CTkButton(self, image=self.cross, text="",
                                    fg_color="transparent", border_width=1,
                                    width=70, height=70, command=self.wrong)
        self.mark_wrong.grid(row=1, column=0, padx=10, pady=10)

        self.mark_right = CTkButton(self, image=self.check, text="",
                                    fg_color="transparent", border_width=1,
                                    width=70, height=70, command=self.right)
        self.mark_right.grid(row=1, column=1, padx=10, pady=10)
        self.wrong()

    def right(self) -> None:
        """handle right answer"""
        self.next_card(True)

    def wrong(self) -> None:
        """handle wrong answer"""
        self.next_card(False)

    def next_card(self, add_back: bool) -> None:
        """brings up the next word"""
        self.current_data = self.data.next_data(add_back)
        self.show_french.configure(text="French\n"
                                   f"{self.current_data[0]}")
        self.show_english.grid_forget()
        self.show_french.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.after(5000, self.flip_card)
        

    def flip_card(self) -> None:
        """flip card to show back card"""
        self.show_english.configure(text="EngLish\n"
                                    f"{self.current_data[1]}")
        self.show_french.grid_forget()
        self.show_english.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


if __name__ == "__main__":
    app = FlashCardUI()
    app.mainloop()
