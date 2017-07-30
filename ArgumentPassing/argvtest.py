# Look at sys module to see what it it does
import sys

print(sys.argv) # prints a list containing the name of the python file
'''
operators = {
                'add':(lambda a,b: a + b),
                'sub':(lambda a,b: a - b),
                'mul':(lambda a,b: a * b),
                'div':(lambda a,b: a / b)
            }
            
operator, value1, value2 = sys.argv[1:]
value1 = float(value1)
value2 = float(value2)
print(operators[operator](value2,value2))'''