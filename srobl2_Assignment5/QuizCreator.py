#Sheila Robles
#Assignment 5 Part 1b
#Python Version 3.0.1

import csv

student_name = ""

def store_student_answer(question_number, answer, correct_or_not):
    global student_name
    # open test bank in append mode to save question information
    with open('testbank_stud_ans.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([student_name,question_number,answer, correct_or_not])

        
def display_question(q_number, quest, sol):
    # display the question one by one for user to answer
    correct_or_not = "Wrong"
    print("Question", q_number, "")
    new_quest = ""
    #for char in quest:
    #    new_quest += char       
    print(str(quest))
    answer = input("YOUR ANSWER: ")
    print("\n")
    if answer.lower == sol.lower:
        correct_or_not = "Correct!"
    store_student_answer(q_number, answer, correct_or_not)
    

def retrieve_questions_for_quiz():
    #try:
        with open('testbank.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            #headers = next(csv_reader)
            for row in csv_reader:
                if row != []:
                    question_number, question, solution = row
                    display_question(question_number, question, solution)
    #except FileNotFound as fnf:
     #   print(fnf)
      #  print("No file named testbank.csv in current working directory")
        
    
if __name__ == "__main__":
    student_name = input("Enter your name. ")
    retrieve_questions_for_quiz()
    
