#Sheila Robles
#Assignment 2 Problem 3
#Python Version 3.0.1

# Collatz Sequence
# If a number, N, is divisible by 2 then divide it by 2.
# If a number, N, is not divisible by 2 then multiply it by 3 and add 1.
# Stop when the number, N, is 1. 

def collatz_sequence(num, seq_str):
	while num != 1:
		if num % 2 == 0:
			num = int(num / 2)
		else:
			num = num * 3 + 1
		seq_str = seq_str + " " + str(num)
	print(seq_str)
	
# initialize the variables and check for negative number. Once all is clear
# call the function to start the sequence.
seq_string = input("Enter a number: ")
number = int(seq_string)

if number <= 0:
	print("Sorry, your number cannot be negative or zero. Please rerun and try again.")
else:
	collatz_sequence(number, seq_string)
