class Person :
    def __init__(self,first,last):
        self.firstname=first;
        self.lastname=last;
        print ( "Base costructor called")

    def __str__(self):
        return self.firstname + " " + self.lastname



class Employee (Person) :

    def __init__(self,first,last, empid):
        Person.__init__(self,first,last);
        self.employeeid=empid;
        print("derived constructor called")

    def getEmployee(self):
        return str(self.employeeid) + " " + self.firstname

    def __str__(self):  #overridden the __str__ method
        return Person.__str__(self)+ " "+str(self.employeeid)


#p= Person("Anil", "Patil")
e= Employee("Sunil","Patil",2000)
#print(p)
print(e)

print(e.getEmployee())

#emp=Employee("Sunil","Patil",300)
#print(emp.name())
#print(emp.getEmployee())


