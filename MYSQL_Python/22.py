import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)
mycursor = mydb.cursor()

# one way
sql = "UPDATE solar SET address = %s WHERE address = %s"
val = ("Hitech City", "Kphb 6")
mycursor.execute(sql,val)
'''
sql = "UPDATE solar SET address = 'Hitech city' WHERE address = 'Kphb 9'"

mycursor.execute(sql)
'''
mydb.commit()

print(mycursor.rowcount, "record(s) affected")




