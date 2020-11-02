import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

sql = "DELETE FROM solar WHERE address = %s"
v1 = input('Enter user add : ')
adr = (v1, )

mycursor.execute(sql,adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


