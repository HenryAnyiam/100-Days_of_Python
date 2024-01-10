#!/usr/bin/python3
"""password manager module"""

from customtkinter import *
from tkinter import messagebox
from PIL import Image
import pyperclip
from passwordmanager import PasswordManager


class PasswordManagerUI(CTk):
    """UI for password manager"""

    def __init__(self, location: str) -> None:
        super().__init__()
        self.title("Password Manager")
        self.password_manager = PasswordManager(location)
        self.configure(fg_color="white", padx=50, pady=50)

        self.load_image = Image.open("./logo.png")
        self.image = CTkImage(light_image=self.load_image, size=(200, 200))
        self.image_label = CTkLabel(self, image=self.image, text="")
        self.image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.website = CTkLabel(self, text="Website:",
                                font=("Times New Roman", 20))
        self.website.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.website_entry = CTkEntry(self, width=300)
        self.website_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.website_entry.focus()

        self.email = CTkLabel(self, text="Email/Username:",
                              font=("Times New Roman", 20))
        self.email.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.email_entry = CTkEntry(self, width=300)
        self.email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        self.password = CTkLabel(self, text="Password:",
                                 font=("Times New Roman", 20))
        self.password.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.password_entry = CTkEntry(self, width=155)
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        self.generate = CTkButton(self, text="Generate Password", width=135,
                                  command=self.generate_password)
        self.generate.grid(row=3, column=2, padx=5, pady=5)

        self.add_details = CTkButton(self, text="Add", width=300,
                                     command=self.save_details)
        self.add_details.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    def save_details(self) -> None:
        """save details to json file"""
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if website and email and password:
            details = {
                "website": website,
                "email": email,
                "password": password
            }
            self.password_manager.save_password(details)
            self.website_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.password_entry.delete(0, END)
            messagebox.showinfo(title="Password Manager",
                                message="Details Saved Successfully")
        else:
            messagebox.showerror(title="Error", message="Empty Fields Exists\n"
                                 "Fill up all Fields to Continue")

    def generate_password(self) -> None:
        """generate random password and insert to password entry"""
        password = self.password_manager.generate_password()
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)


if __name__ == "__main__":
    app = PasswordManagerUI("password.json")
    app.mainloop()
