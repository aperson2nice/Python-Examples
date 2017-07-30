from __future__ import print_function

def add_q_to_db(string):
    # add question to database or csv
    return ""
    
def generate_string(question, answer, ):
    return ""
    
def get_question(number):
    a = input("Enter question: " + str(number+1) + ":")
    return a

    
def get_answers(num_of_choices): # works fine
    answer_choices = ""
    for n in range(num_of_choices):
        answer_choices += raw_input("Enter answer choice " + str(n+1) + ": ") + "\n"
    return answer_choices
    
def start_question(number):
    string = ""
    q_type = raw_input("What type of question is this? ")
    if q_type == "MC" or "mc":
        string += "'" + str(number+1) + ". Multiple Choice\n"
        num_of_ac = raw_input("How many answer choices?")
        string += get_question(number)
        string += get_answers(num_of_ac)
            

    
    elif q_type == "OE" or "oe":
        string += "'" + str(number+1) + ". Open Ended\n"
        question = OEQuestion(q_type, number, question, answer)
        
    elif q_type == "TF" or "tf":
        string += "'" + str(number+1) + ". True or False\n"
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
    
    
    
    
    
    
    
    