import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)


mycursor = mydb.cursor()

#sql = "SELECT * FROM solar WHERE name LIKE 'a%'"
sql = "SELECT * FROM solar WHERE name LIKE '%s'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
  
  
  