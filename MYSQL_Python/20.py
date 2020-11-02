import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

sql = "DELETE FROM solar WHERE address ='Kphb 8'"
#sql = "DELETE FROM solar"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")




