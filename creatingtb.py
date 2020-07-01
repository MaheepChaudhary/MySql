import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",      
                               passwd = "M@heep1234",
                               database = 'testdb'   
                              )

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Student (name VARCHAR(100), age INTEGER(3))")


#for db in mycursor:
#  print(db)