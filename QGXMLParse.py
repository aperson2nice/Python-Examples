from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

testBank = ""
questions = Element("Questions")

def question_to_XML(comment,q_type, q_number, a_choice = None, the_answer):
    #p_comment = Comment(comment) # comment shoud be
    question = SubElement(questions, question_type=q_type, Question_Number=q_number)
    if q_type == "MC" or q_type == "TF": # check if it's a multiple choice question
        if q_type == "TF":
            answerchoice = SubElement(question, a_choice) # repeat for each choice
        else:
            for a in answer:
                # prompt user for answer
                answerchoice = SubElement(question, a_choice) # print to the document
    answer = SubElement(question, the_answer+"**")


def pretty_xml_printout(question):
    reparsed = minidom.parseString(tostring(question))
    return reparsed.toprettyxml(indent="     ")
    
