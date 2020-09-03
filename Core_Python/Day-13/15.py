# function
# function return type 
username = input('Enter user name : ')
password = input('Enter user password : ')

def login():
    user = 'micky'
    pwd = 'python123'
    if user == username and pwd == password:
       return 'yes'
    else:
        print('Login Failed') 

def deposite():
    if login() == 'yes':
        amount = float(input('Enter amount to deposite : '))
        m_amount = 5000
        bal = m_amount +amount
        print()
        print('Total Amount is : ',bal)
    else:
        print('Try Again')

v1 = input('Would you like to deposite amount : ')
if v1 == 'yes':
    deposite()
else:
    print('Tank you')




