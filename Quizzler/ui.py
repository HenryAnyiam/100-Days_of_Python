#!/usr/bin/python3
"""Quiz app UI"""

from typing import Optional, Tuple, Union
from customtkinter import CTk, CTkLabel, CTkButton, CTkImage
from PIL import Image
from quiz_brain import QuizBrain


class QuizUI(CTk):
    """UI for the quiz"""

    def __init__(self, quiz_handle: QuizBrain) -> None:
        super().__init__()
        self.title("Quizzler")
        self.quiz_handler = quiz_handle
        self.configure(fg_color="#375362", padx=20, pady=20)

        self.score_label = CTkLabel(self, text="Score: 0", text_color="white")
        self.score_label.grid(row=0, column=1, padx=10, pady=10)

        self.question_label = CTkLabel(self, text="",
                                       width=300, height=250,
                                       font=("Arial", 20, "italic"),
                                       bg_color="white", wraplength=270,
                                       text_color="#375362")
        self.question_label.grid(row=1, column=0, columnspan=2,
                                 padx=10, pady=10)

        wrong = CTkImage(light_image=Image.open("./images/false.png"),
                         size=(70, 70))
        right = CTkImage(light_image=Image.open("./images/true.png"),
                         size=(70, 70))

        self.wrong_check = CTkButton(self, image=wrong, text="",
                                     width=70, height=70,
                                     fg_color="transparent",
                                     command=self.answer_false)
        self.wrong_check.grid(row=2, column=0, padx=10, pady=10)

        self.right_check = CTkButton(self, image=right, text="",
                                     width=70, height=70,
                                     fg_color="transparent",
                                     command=self.answer_true)
        self.right_check.grid(row=2, column=1, padx=10, pady=10)
        self.next_question()

    def next_question(self):
        """serve up next question"""
        self.question_label.configure(fg_color="white")
        if not self.quiz_handler.still_has_questions():
            self.question_label.configure(text="No More Questions")
        else:
            question = self.quiz_handler.next_question()
            self.question_label.configure(text=question)
            score = f"Score: {self.quiz_handler.score}"
            self.score_label.configure(text=score)

    def answer_true(self):
        """answer true to question"""
        self.flash_color(self.quiz_handler.check_answer("True"))

    def answer_false(self):
        """answer false to question"""
        self.flash_color(self.quiz_handler.check_answer("False"))

    def flash_color(self, flash: bool):
        """flash color"""
        if flash and self.quiz_handler.still_has_questions():
            self.question_label.configure(fg_color="green")
        elif self.quiz_handler.still_has_questions():
            self.question_label.configure(fg_color="red")
        self.after(200, self.next_question)
