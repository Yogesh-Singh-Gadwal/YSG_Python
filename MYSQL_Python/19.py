import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

#sql = "SELECT name FROM solar ORDER BY name"
sql = "SELECT name FROM solar ORDER BY name DESC"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
  
  
  