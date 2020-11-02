import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="universe"
)

mycursor = mydb.cursor()

sql = "INSERT INTO solar (name, address) VALUES (%s, %s)"
val = [
  ('Rohit', 'Kphb 1'),
  ('Shekhar', 'Kphb 2'),
  ('Sai Kiran', 'Kphb 3'),
  ('Rohan', 'Kphb 4'),
  ('Sandy', 'Kphb 5'),
  ('Akhil', 'Kphb 6'),
  ('Arjun', 'Kphb 7'),
  ('Shikha', 'Kphb 8'),
  ('Vicky', 'Kphb 9'),
  ('Jatain', 'Kphb 10'),
  ('Akira', 'Kphb 11'),
  ('Srinivas', 'Kphb 12'),
  ('Varnika', 'Kphb 13')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")









