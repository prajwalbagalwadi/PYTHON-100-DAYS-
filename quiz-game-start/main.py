# JAI SHREE RAM 
#RULES:This is quiz game you will get +1 points for correct answer and -1 points worng answer respectively 
# importing file 
from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

#creating empty list
question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_ans=question["answer"]
    new_question=Question(question_text, question_ans)
    question_bank.append(new_question)
    
quiz=Quiz_Brain(question_bank)
while quiz.question_left():
    
    quiz.next_question()

print("quiz is completed\n")
print(f"your final score{quiz.score}|{quiz.question_number} ")
if(quiz.score<5):
    print("you lost")
