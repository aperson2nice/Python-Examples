#Sheila Robles
#Assignment 3 Problem 1
#Python Version 3.0.1
#Modification of Point class

class Point(object):
    ''' A point on a grid at location x, y '''
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
    def __str__(self):
        return "X=" + str(self.X) + " Y=" + str(self.Y)

    def __add__(self, other):
        if not isinstance(other,(Point,list,tuple)):
            raise TypeError("Must be of type Point")
        if isinstance(other,(list,tuple)):
            x = self.X + other[0]
            y = self.Y + other[1]
            return Point(x,y)
        x = self.X + other.X
        y = self.Y + other.Y
        return Point(x,y)


if __name__ == "__main__":
    p1 = Point(5,8)
    p2 = Point(10,7)
    print("Testing the print statements of p1 and p2.")
    print(p1)
    print(p2)

    print("Testing the add function with a Point")
    p3 = p1 + p2
    print(p3)
    
    print("Testing the add method with a tuple and then a list")
    print(p1 + (3,5.5),"Should be (8,13.5)")
    print(p2 + [3,5], "Should be (13,12)") 