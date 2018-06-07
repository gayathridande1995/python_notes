import sqlite3
conn = sqlite3.connect('test.db')
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit
print ("Total number of rows updated :", conn.total_changes)

cursor1 = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor1:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.close()
