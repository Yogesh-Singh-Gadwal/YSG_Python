import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

sql = "INSERT INTO solar (name, address) VALUES (%s, %s)"
val = ("Harsha", "Jntu")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
print(mycursor.rowcount, "was inserted.")



