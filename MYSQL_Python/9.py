import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)


mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE pluto ADD COLUMN id INT(2) AUTO_INCREMENT PRIMARY KEY")
