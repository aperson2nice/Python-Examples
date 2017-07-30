#Sheila Robles
#Assignment 5 Part 1a
#Python Version 3.0.1

import csv

question_number = 0
def append_question_to_csv(number, question, solution):
    # open test bank in append mode to save question information
    with open('testbank.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([number,question,solution])

def make_mc_question():
    # Make a multiple choice question
    global question_number
    question_number += 1
    question = input("Enter question: ") + "\n"
    num_of_answer_choices = int(input("Enter number of answer choices: "))
    #Generate the answer choices
    answer_choices = ""
    letters = ['a','b','c','d','e','f','g','h']
    for num in range(num_of_answer_choices):
        answer_choices += "      " + letters[num] + ". " + input("Enter answer choice " \
                          "" + letters[num] + ": ") + '\n'
    solution = input("What is the answer?  ")
    print("\n")
    #Generate the final question string and save it to the csv by calling function
    final_question = ("Multiple Choice: \n" + "   " + question + answer_choices)
    print(final_question)
    append_question_to_csv(question_number, final_question , solution)

def make_tf_question():
    # Make a true/false question
    global question_number
    question_number += 1
    question = input("Enter statement: ")
    solution = input("What is the answer? ")
    print("\n")
    final_question = "True of False: \n" + "   " + question
    print("\n")
    append_question_to_csv(question_number, final_question , solution)
    
def make_oe_question():
    # Make an open ended question
    global question_number
    question_number += 1
    question = input("Enter question: ")
    solution = input("What is the answer? ")
    print("\n")
    final_question = "   Open Ended: \n" + "   " + question
    print("\n")
    append_question_to_csv(question_number, final_question , solution)
    
if __name__ == "__main__":
    number_of_questions = int(input("Enter the number of questions: "))
    to_stop = True;
    while to_stop and number_of_questions > 0:
        q_type = input("\n-----MC for Multiple Choice\n-----OE for Open"\
                " Ended\n-----TF for True, False. To stop type STOP > ")
        print("\n")
        if q_type in ['MC','Mc','mC','mc']: make_mc_question()
        elif q_type in ['TF','Tf','tf','tF']: make_tf_question()
        elif q_type in ['OE','Oe','oe','oE']: make_oe_question()
        elif q_type == "STOP": to_stop = False
        else: 
            print("Invalid Submission Type. Try again.\n")
            number_of_questions += 1
        number_of_questions -= 1
                         
    print("Thank you or creating a test!")

