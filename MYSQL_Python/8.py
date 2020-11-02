import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE solar(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), address VARCHAR(55))")

