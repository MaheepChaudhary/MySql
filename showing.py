import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",      
                               passwd = "M@heep1234",
                               database = 'testdb'   
                              )

mycursor = mydb.cursor()
          
mycursor.execute("SELECT * FROM Student")

myresult = mycursor.fetchall()

for row in myresult:
  print(row)