class Parent :
    parentattr =100
    def __init__(self):
        print("constructor Parent called")

    def parentmethod(self):
        print( "calling parent method")

    def setAttr(self,attr):
        Parent.parentattr=attr

    def getAttr(self):
        print("Parent attribute", Parent.parentattr)

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child contructor called")
    def childMethod(self):
        print("child method called")


c=Child()
c.parentmethod()
c.childMethod()
c.setAttr(20)
c.getAttr()

