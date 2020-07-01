import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",      
                               passwd = "M@heep1234"   
                              )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdb")


#for db in mycursor:
#  print(db)