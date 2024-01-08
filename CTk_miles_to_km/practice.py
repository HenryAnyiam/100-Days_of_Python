#!/usr/bin/python3

import customtkinter


window = customtkinter.CTk()
window.title("GUI Application")
window.minsize(width=500, height=300)

my_label = customtkinter.CTkLabel(window, text="I Am A Label",
                                  font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

my_label.configure(text="New Text")

num = 1


def click_button():
    global num
    new_label = customtkinter.CTkLabel(window, text=f"Click Number {num}",
                                       font=("Arial", 24, "bold"))
    my_label.configure(text="Button got clicked"
                       f" {num} time{'' if num < 2 else 's'}")
    num += 1
    new_label.pack(pady=5)


my_button = customtkinter.CTkButton(window, text="Click Me",
                                    command=click_button)
my_button.grid(row=1, column=1)


my_entry = customtkinter.CTkEntry(window)
my_entry.grid(row=2, column=3)


def get_entry():
    entry = my_entry.get()
    my_entry.delete(0, len(entry))
    my_label.configure(text=entry)


sec_button = customtkinter.CTkButton(window, text="Get Entry",
                                     command=get_entry)
sec_button.grid(row=0, column=2)

window.mainloop()
