import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

l1 = []
for x in mycursor:
  #print(x)
  l1.append(list(x))
#print(l1)


v1 = input('Enter database name : ')
for y in l1:
    for z in y:
        #print(z)
        if z == v1:
           print('Data Base is Present')
           
           
           
        
        
    
    

  
   
