#Sheila Robles
#Assignment 2 Problem 1
#Python Version 3.0.1

def frequency_counter(string):
    # counts the frequcy of each character in string
    # store count in a dictionary
    letter_frequency = {}
	
    for character in string:
        if character not in letter_frequency:
            letter_frequency[character] = 0
        letter_frequency[character] += 1
    return(letter_frequency)
	
def file_or_direct():
    # ask user for a file or text input 
    f_or_d = input("File or direct: ")
    if(f_or_d == "File" or f_or_d == "file"):
        #Open the file and read
        file_name = input("File name:") 
        read_file = open(file_name, "r")
        text = read_file.read()
        read_file.close()
    else:
        #Read the line of text inputted
        text = input("Text: ")
    return text

text = file_or_direct()
print(frequency_counter(text))
