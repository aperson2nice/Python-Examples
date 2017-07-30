from __future__ import print_function

class QuizGenerator(object):
    num_of_questions = ""
    problem_number = 0        
                
class Question(object):
    ''' A question in a quiz '''
    def __init__(self, q_type, problem_number, question, answer):
        self.q_type = q_type
        self.problem_number = problem_number
        self.question = question
        self.answer = answer

class MCQuestion(Question,answers):
    def __init__(self, q_type, problem_number, question, answer):
        Question.__init__(self, q_type, problem_number, question, answer)
    def __str__(self):
        return "Multiple Choice Question: \nProblem " + \
                str(self.problem_number) + ": " + self.question + "\n" \
                + "."
        
class TFQuestion(Question):
    def __init__(self, q_type, problem_number, question, answer):
        Question.__init__(self, q_type, problem_number, question, answer)
    def __str__(self):
        return "True/False Question: \nProblem " + \
                str(self.problem_number) + ": " + self.question + "\n" \
                + "."
                            
class OEQuestion(Question):
    def __init__(self, q_type, problem_number, question, answer):
        Question.__init__(self, q_type, problem_number, question, answer)
    def __str__(self):
        return "Open Ended Question: \nProblem " + \
                str(self.problem_number) + ": " + self.question + "\n" \
                + "."

def make_question(q_type):
    string = ""
    if q_type == "MC" or "mc":
        string += "Multiple Choice\n"
        question = raw_input("Enter question: ")
        question = MCQuestion(q_type, number, question, answer)
    elif q_type == "OE" or "oe":
        question = OEQuestion(q_type, number, question, answer)
    elif q_type == "TF" or "tf":
        question = TFQuestion(q_type, number, question, answer)
    else:
        question = "Invalid question type"

def add_question_to_DB(question):
    question.__str__() # add question to database                                    
                                                                                                    
def createQuestion(number):
    q_type = raw_input("Enter your question type: MC for Multiple Choice, OE for Open Ended, TF for True, False ")
    question = raw_input("Enter question: ")
    answer = raw_input("What is the answer? ") 
    
   
if __name__ == "__main__":
    # while loop prompt user to enter number of qs. Prompt for type
    # of question each time.
    num_of_questions = input("Enter the number of questions ")
    for number in range(num_of_questions):
        question_string = str(number)+","
        question_string += createQuestion(number)+"\n"
        # add question_string to csv file
        
    
    print("Thank you, you have completed your test")
    
    
    
    
    
    
    
    