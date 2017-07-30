#Sheila Robles
#Assignment 3 Problem 3
#Python Version 3.0.1

# Look at argparse on the documentation for more exposure
# addArgument(), action(), inargs() recommended to look at

import argparse

def locator():
    #The primary part of the code

    
parser = argparse.ArgumentParser(description="This is a program that will take a string and navigates the file system looking for either a file or directory with the name of the string that was passed")
parser.add_argument("Root", type=dir, help="This is the root directory to start looking",
                    required=True)
parser.add_argument("String", type=str, nargs='*', help="The string used to search for file or directory",
                    required=True)
# What is a positional argument????
parser.add_argument("-f", "--file", type=list, help="Forces the program to use only lists.",
                    required=False)
parser.add_argument("-d", "--directory", type=list, nargs='*', help="Will force the program to only list directories",
                    required=False)
parser.add_argument("-m", "--last-modified", type=str, nargs='*', help="The time the file was last modified",
                    required=False)
                                
args = parser.parse_args()

print(type(args))
#print(operate(operators[args.operation], args.values))