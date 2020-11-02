# Final
import mysql.connector 

mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="root",
       database="universe")
       
mycursor = mydb.cursor()

print("*"*40)
print()

print("Welcome to Universal Bank")
print()

l1 = ["s1 : Create_Account","s2 : Deposite_Amount","S3: Amount_Status","s4 : Withdraw_AMount"] 

print("Hi,Are you Looking for which service : ",l1)

print()

v1 = input("Enter your service code : ")

if v1 == 's1':
    sql1 = "insert into ubank(name,city,country,amount,phone,email) values(%s,%s,%s,%s,%s,%s)"
    c1 = input("Enter user name : ")
    c2 = input("Enter user city : ")
    c3 = input("Enter user country : ")
    c4 = float(input("Enter user amount : "))
    c5 = input("Enter user phone : ")
    c6 = input("Enter user email : ")
    val = (c1,c2,c3,c4,c5,c6)
    mycursor.execute(sql1,val)
    mydb.commit()
    print()
    print(mycursor.rowcount,' : Record is Inserted')
    print()
    print("Your Inserted Record ID Value is : ",mycursor.lastrowid)
elif v1 == 's2':
   pass
elif v1 == 's3':
   pass
elif v1 == 's4':
   pass
else:
   print('Present Service is not Available...')
   
   
   
# CREATE 
# INSERT 
# Deposite 
# Status 
# Withdraw 
# if amount is withdraw from date of 7-31 in between then no intreset 
#  but if amount is withdraw from 1 - 7 then rate of interest is 2% at end of the month

# if u have deposite money before 1-7 then only u will get 2% interest


   
   
   
   
   
   
   
   
   
   
   