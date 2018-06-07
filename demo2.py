class Point :
    """ Point class, represents point in x, y coord"""

    def __init__(self,x1=5,y1=7):
        print("Constructor called")
        self.x=x1
        self.y=y1

    def print(self):
        print(" X Cord: ", self.x ," y coord :", self.y)

    def __del__(self):
        print("Destructor called")

    def __str__(self):
        return "This is from str function"

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)






