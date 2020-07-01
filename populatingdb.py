import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",      
                               passwd = "M@heep1234",
                               database = 'testdb'   
                              )

mycursor = mydb.cursor()

sqlformula = "INSERT INTO Student (name,age) VALUES  (%s,%s)"
students = [("Raechel",22),("Bob",48),("Maheep",24)] 
           

mycursor.executemany(sqlformula,students)
mydb.commit()



#for db in mycursor:
#  print(db)