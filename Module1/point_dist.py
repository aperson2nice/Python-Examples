from math import sqrt

#Accepts two tuples that represents
#points on a graph and calculates the
#distance between them.
def distance(coor1, coor2):
    assert (len(coor1) == 2), "First parameter not a point on a 2D graph. " + coor1
    assert (len(coor2) == 2), "Second parameter not a point on a 2D graph. " + coor2
    
    #Unpacks the elements from coor1 and assigns them
    #to x1 and y1 respectively (same for the next line)
    x1, y1 = coor1
    x2, y2 = coor2
    
    x_distance = (x1 - x2) ** 2
    y_distance = (y1 - y2) ** 2
    distance = sqrt(x_distance + y_distance)
    
    return distance

#Python 3 users should change raw_input to input    
first_coordinates = raw_input("Enter the first coordinates separated by a space: ").split()
second_coordinates = raw_input("Enter the second coordinates separated by a space: ").split()

#Convert the input to a number type.
first_coordinates = [float(i) for i in first_coordinates]
second_coordinates = [float(i) for i in second_coordinates]

#Python 3 users should change the print statement to a print function
print distance(first_coordinates, second_coordinates)





