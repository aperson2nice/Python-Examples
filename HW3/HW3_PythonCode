# Look at argparse on the documentation for more exposure
# addArgument(), action(), inargs() recommended to look at

import argparse

def operate(func, lst_of_values):
    ans = lst_of_values[0]
    for value in lst_of_values[1:]:
        ans = func(ans, value)
    return ans

operators = {
                'add':(lambda a,b: a + b),
                'sub':(lambda a,b: a - b),
                'mul':(lambda a,b: a * b),
                'div':(lambda a,b: a / b)
            }
    
parser = argparse.ArgumentParser(description="This is a useful program for doing basic mathematical operations")
parser.add_argument("-o", "--operation", type=str, help="Pass and operation: add, mul, sub, div",
                    required=True)

# What is a positional argument????
parser.add_argument("-v", "--values", type=float, nargs='*', help="Pass in multiple numbers separated by a space",
                    required=True)
                                
args = parser.parse_args()

print(type(args))
#print(operate(operators[args.operation], args.values))