import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM solar WHERE address ='Kphb 6'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
  
  
  
  