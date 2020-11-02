import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM solar")

myresult = mycursor.fetchone()
#myresult = mycursor.fetchall()
print(myresult)



