#operator overloading

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.__z=3  #private member
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)
    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)

    def getz(self):  #private member accessible through this method
         return self.__z;

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2,3)

#p1.__Z   -> not accessible as __z is private

print(p1.getz())
p2 = Point(3,4)
p3=p1+p2
print(p3)

'''
print (p1 + p2) 	#prints (5, 7)
print (p1 * p2) 	#prints (6, 12)
print (p1 * 2) 	#prints (4, 6)
'''
