#!/usr/bin/python3
"""Module for quiz mechanics"""


class QuizBrain:
    """The mchanics handler"""

    def __init__(self, questions: list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def still_has_questions(self):
        """checks if there are still questions"""
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        """return the next question"""
        num = self.question_number
        question = self.question_list[num]
        answer = input(f"Q.{num + 1}: {question.text} (True/False)?:")
        self.question_number += 1
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """check if an answer is correct"""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"Your score is {self.total_score()}\n")

    def total_score(self):
        """return final score"""
        return f"{self.score}/{self.question_number}"
