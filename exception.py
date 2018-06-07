try :
    print(5/0)
except ZeroDivisionError:
    print("Division by zero occured")

except Exception :
    print("Exception Occured")
else :
    print("In else part")
finally :
    print(" Excecute inspite of exception or no")

print("Hello")

