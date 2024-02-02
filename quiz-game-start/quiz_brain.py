class Quiz_Brain:
    def __init__(self,qlist):
        self.question_number=0
        self.score=0    
        self.question_list= qlist
        
    def question_left(self):
        return self.question_number<len(self.question_list)
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}-->>{current_question.question_text} (T/F):>>")     
        self.check_answer(user_ans,current_question.answer)
    
    def check_answer(self,user_ans,correct_ans):
        
        if user_ans.lower()==correct_ans.lower():
            self.score=self.score+1
            print("+1")
        
        if user_ans.lower()!=correct_ans.lower():
             self.score-=1
             print("-1")
        print(f"The correct answer was: {correct_ans}.")    
        print(f"SCORE==>{self.score}---{self.question_number}")    