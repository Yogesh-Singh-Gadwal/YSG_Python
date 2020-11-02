import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
  
print()
print()
  
mycursor.execute("desc pluto")
for x in mycursor:
  print(x)
  
  