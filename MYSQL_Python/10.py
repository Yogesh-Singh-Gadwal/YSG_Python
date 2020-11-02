from time import sleep
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()
# ---------------------------------
sql = "INSERT INTO pluto (name, address) VALUES (%s, %s)"
v1 = input('Enter user name : ')
v2 = input('Enter user address : ')

val = (v1, v2) 
mycursor.execute(sql, val)

sleep(10)
print('Hello Micky.......')
sleep(5)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
