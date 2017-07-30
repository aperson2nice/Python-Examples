problem_number = 0

def CreateOEQuestion():
    global problem_number
    problem_number += 1
    oe_question = input("Enter question "+str(problem_number)+": ")
    answer = input("What is the answer? ")
    # Add question to DB with problem_number

def CreateMCQuestion():
    global problem_number
    num_of_choices = input("How many answer choices do you want? ")
    problem_number += 1
    MC_numbers = ["a.","b.","c.","d.","e.","f."]
    mc_question = input("Enter question " + str(problem_number) + ": ")
    for choice in range(num_of_choices):
        a_choice = input("Enter answer choice",MC_numbers[choice])
    answer = input("What is the answer? (a,b,c,d,e,f): ")
    # Add question to DB with problem_number 

def CreateTFQuestion():
    global problem_number
    tf_question = input("Enter question " + str(problem_number) + ": ")
    answer = input("What is the answer?")
    # Add question to DB with problem_number 

def QuestionType():
    print("What is your question type?")
    q_type = input("MC for Multiple Choice, OE for Open Ended", "TF for True, False")
    if q_type == "MC":
        CreateMCQuestion()
    elif q_type == "OE":
        CreateOEQuestion()
    elif q_type == "TF":
        CreateTFQuestion()
    else:
        print("Invalid question type")
        

