import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT id,name FROM solar")

#mycursor.execute("SELECT name FROM solar")


sql1 = "SELECT name,address FROM solar where id = %s"
v1 = int(input('Enter Search Recored : '))
mycursor.execute(sql1,(v1,))


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  

  
  
  
  