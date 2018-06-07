import re
'''
expression= "Python is easy to learn"
result=re.findall(r"^\w+",expression)
print(result)

print(re.split(r"\s",expression))

######
list=["Python","is","easy","to","learn"]
for element in list:
    z=re.match(r"is",element)
    if z :
        print("Match Found")
         print(z.groups())
'''
abc='@gmail.com, abc99@hotmail.com, users@yahoomail.com'
emails= re.findall(r"[\w\.-]+@[\w\.-]+",abc)
for email in emails:
    print(email)
