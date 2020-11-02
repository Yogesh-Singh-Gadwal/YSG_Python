from time import sleep
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()

mycursor.execute("show databases")

for x in mycursor:
    print('Data Base Name is : ',x)

print()
sleep(3)

mycursor.execute("CREATE DATABASE universe")

sleep(2)
mycursor.execute("show databases")

for x in mycursor:
    print('Data Base Name is : ',x)     
     






