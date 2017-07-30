#Sheila Robles
#Assignment 3 Problem 2
#Python Version 3.0.1

class Bag(object):
    def __init__(self):
        self.contents = []
    
    def put_in_bag(self,object):
        self.contents.append(object)

    def __str__(self):
        return "The contents of the bag are are: " + str(self.contents)


if __name__ == "__main__":
    bag1 = Bag()
    bag2 = Bag()
    bag1.put_in_bag("comb")
    bag1.put_in_bag("candy bar")
    print(bag1)
    print(bag2)