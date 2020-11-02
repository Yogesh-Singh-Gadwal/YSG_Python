import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM solar LIMIT 5")

mycursor.execute("SELECT * FROM solar LIMIT 5 OFFSET 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
  
  