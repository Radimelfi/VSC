
from data import question_data 
from question_model import Question 
from quiz_brain import QuizBrain

question_quiz = []
for question in question_data:
    question_text = question ["text"]
    question_answer = question ["answer"]
    new_question = Question(question_text, question_answer)
    question_quiz.append(new_question)
    print(new_question)
    

quiz = QuizBrain(question_quiz)

while quiz.still_has_question():
    quiz.next_question()
print (f"you've completed the quiz")
print (f"your final score was: {quiz.score}/{len(question_data)}")

