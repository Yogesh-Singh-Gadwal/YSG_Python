import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()
#print(mycursor)
mycursor.execute("create table pluto(name VARCHAR(20), address VARCHAR(50))")
