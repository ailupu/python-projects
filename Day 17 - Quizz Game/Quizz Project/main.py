from question_model import Question
from data import question_data
from quizz_brain import QuizzBrain

question_bank = []

for el in question_data:
    question_bank.append(Question(el['text'], el["answer"]))

quiz = QuizzBrain(question_bank)

while quiz.still_has_question():# if quizz has question continue
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


