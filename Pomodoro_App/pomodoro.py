#!/usr/bin/python3
"""build a pomodoro timer"""

from customtkinter import *
from PIL import Image


class Pomodoro(CTk):
    """The pomodoro UI"""

    def __init__(self, font_name: str) -> None:
        super().__init__()
        self.title("Pomodoro")
        self.curr_time = None
        self.timings = ["25:00", "05:00"]
        self.time_color = [
            ("Work Time", "#9bdeac"),
            ("Short Break", "#e2979c"),
            ("Long Break", "#FF6347")]
        self.font = font_name
        self.configure(padx=50, pady=50, fg_color="#f7f5dd")
        self.timer_label = CTkLabel(self, text="Timer",  text_color="#9bdeac",
                                    font=(self.font, 50))
        self.timer_label.grid(row=0, column=1)

        self.tomato = CTkImage(light_image=Image.open("./tomato.png"),
                               size=(200, 224))

        self.tomato_label = CTkLabel(self, image=self.tomato, text="")
        self.tomato_label.grid(row=1, column=1)

        self.time_text = CTkLabel(self, text="00:00", text_color="white",
                                  font=(self.font, 35, "bold"),
                                  bg_color="#FF6347")
        self.time_text.grid(column=1, row=1, pady=(50, 0))

        self.start = CTkButton(self, text="Start", corner_radius=5,
                               fg_color="#FF6347",
                               command=self.start_time)
        self.start.grid(column=0, row=2)

        self.reset = CTkButton(self, text="Reset", corner_radius=5,
                               fg_color="#FF6347",
                               command=self.end_time)
        self.reset.grid(column=2, row=2)

        self.check = CTkLabel(self, text="", text_color="#9bdeac",
                              font=(self.font, 30))
        self.check.grid(column=1, row=3)

    def start_time(self) -> None:
        """start app timer"""
        self.curr_time = -1
        self.update_time()
        self.timer_label.configure(text="Work Time",
                                   text_color="#9bdeac",
                                   font=(self.font, 40))

    def end_time(self) -> None:
        """stop and reset time"""
        self.curr_time = None
        self.time_text.configure(text="00:00")
        self.timer_label.configure(text="Timer",
                                   text_color="#9bdeac",
                                   font=(self.font, 50))

    def update_time(self) -> None:
        """update timer"""
        curr_time = self.time_text.cget("text")
        min_sec = curr_time.split(':')
        min_sec = [int(i) for i in min_sec]
        if self.curr_time is not None:
            if min_sec == [0, 0]:
                self.curr_time += 1
                index = self.curr_time % 2
                text = self.timings[index]
                check = self.check.cget("text")
                check = check + "✔" if index == 1 else check
                check = "" if self.curr_time == 0 else check
                if self.curr_time > 6:
                    self.curr_time = -1
                    text = "20:00"
                    index = 2
                timer_text = self.time_color[index][0]
                timer_color = self.time_color[index][1]
                self.timer_label.configure(text=timer_text,
                                           text_color=timer_color)
                self.check.configure(text=check)
            else:
                if min_sec[1] == 0:
                    min_sec[1] = 59
                    min_sec[0] -= 1
                else:
                    min_sec[1] -= 1
                min = min_sec[0] if min_sec[0] > 9 else "0" + str(min_sec[0])
                sec = min_sec[1] if min_sec[1] > 9 else "0" + str(min_sec[1])
                text = f"{min}:{sec}"
            self.time_text.configure(text=text)
            self.after(1000, self.update_time)


if __name__ == "__main__":
    app = Pomodoro(font_name="Courier")
    app.update_time()
    app.mainloop()
