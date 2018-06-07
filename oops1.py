class Point:
    """ Point class manipulates and represents point x, y corodinates"""
    count=0  #class memebr
    def __init__(self, x, y ):
        self.x=x  #instance member
        self.y=y
        Point.count=Point.count+1

    def display(self):
        print("Point x and y are ", self.x ,' ', self.y)

    def CountObj(self):
        print("Number of objects created ", Point.count)

    def __str__(self):
        return "Point X is {0} and Y is {1}".format(self.x,self.y)

    def __del__(self):
        print("Destructor called")



#p2=Point(3,5)
#del(p2)
#p2.CountObj()
p1=Point(2,3)
p1.__setattr__('name','Anil')

#p1.CountObj()

print("Name in object ", p1.name)

p1.__delattr__('name')

print("Name in object ", p1.name)

print(p1)

"""
print(Point.__doc__)
print(Point.__bases__)
print(Point.__name__)
print(Point.__dict__)
#p2.display()
"""
