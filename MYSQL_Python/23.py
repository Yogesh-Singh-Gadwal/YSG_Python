import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)


mycursor = mydb.cursor()

#sql = "DROP TABLE abc"

sql = "DROP TABLE IF EXISTS xyz"


mycursor.execute(sql)


