class QuizBrain:

    def __init__(self, questionlist):
        self.questionnumber=0
        self.questionlist=questionlist
        self.score=0

    def still_has_questions(self):
        return self.questionnumber<len(self.questionlist)


    def next_question(self):
        current_question=self.questionlist[self.questionnumber]
        self.questionnumber+=1
        user_answer=input(f"\nQ.{self.questionnumber}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("Yay! You got it right.")

        else:
            print("This is answer is wrong.")

        print(f"Your current score is {self.score}/{self.questionnumber}")




