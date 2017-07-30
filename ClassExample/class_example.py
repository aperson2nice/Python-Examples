class Point(object):
    ''' A point on a grid at location x, y '''
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
    def __str__(self):
        return "X=" + str(self.X) + " Y=" + str(self.Y)

    def __add__(self, other):
        if not isinstance(other,Point):
            raise TypeError("Must be of type Point")
        x = self.X + other.X
        y = self.Y + other.Y
        return Point(x,y)

if __name__ == "__main__":
    p1 = Point(5,8)
    p2 = Point(10,7)

    print(p1)
    print(p2)

    p3 = p1 + p2
    print(p3)