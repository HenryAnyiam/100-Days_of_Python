#!/usr/bin/python3
"""main file to start quiz"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [Question(i['text'], i['answer']) for i in question_data]


brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()


print("You've Completed the quiz")
print(f"Your final score is {brain.total_score()}")
