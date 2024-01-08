#!/usr/bin/python3
"""A simple miles to km converter"""

from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel


class MilesToKm(CTk):
    """class to hold window"""

    def __init__(self, width: int = 250,
                 height: int = 100, color: str = "red") -> None:
        super().__init__()
        self.minsize(width=width,
                     height=height)
        self.title("Miles To Km Converter")
        self.configure(fg_color=color)

        self.enter_miles = CTkEntry(self)
        self.enter_miles.grid(row=0, column=1, padx=5, pady=5)

        self.miles = CTkLabel(self, text="miles", font=("Times New Roman", 15))
        self.miles.grid(row=0, column=2, padx=5, pady=5)

        self.equal = CTkLabel(self, text="is equal to",
                              font=("Times New Roman", 15))
        self.equal.grid(row=1, column=0, padx=5, pady=5)

        self.result = CTkLabel(self, text="0", font=("Times New Roman", 15))
        self.result.grid(row=1, column=1, padx=5, pady=5)

        self.km = CTkLabel(self, text="Km", font=("Times New Roman", 15))
        self.km.grid(row=1, column=2, padx=5, pady=5)

        self.convert = CTkButton(self, text="convert",
                                 command=self.convert_mile)
        self.convert.grid(row=2, column=1, padx=5, pady=5)

    def convert_mile(self) -> None:
        """convert km to mile and
        write result to screen"""

        user_input = self.enter_miles.get()
        try:
            value = int(user_input)
        except ValueError:
            pass
        else:
            self.result.configure(text=f"{round(value * 1.609, 1)}")
        self.enter_miles.delete(0, len(user_input))


if __name__ == "__main__":
    app = MilesToKm()
    app.mainloop()
