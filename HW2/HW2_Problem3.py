#Sheila Robles
#Assignment 2 Problem 3
#Python Version 3.0.1

import random

def addingGame():
	# generate random addition problems for the user to
	# guess until the user guesses wrong
	correct_solutions = 0
	value1 = random.randint(1,101)
	value2 = random.randint(1,101)
	answer = value1 + value2
	guess = int(input(str(value1)+"+"+str(value2)+"="))

	while guess == answer:
		print("Correct!")
		correct_solutions += 1
		value1 = random.randint(1,101)
		value2 = random.randint(1,101)
		answer = value1 + value2
		guess = int(input(str(value1) + "+" + str(value2) + "="))
	print("Correct Solutions: ", correct_solutions)
	
addingGame()

input("Press ENTER to continue.") # wait before ending the program