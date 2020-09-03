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
        print()
        print('Welcome to Deposite Section ..')
        amount = float(input('Enter amount to deposite : '))
        m_amount = 5000
        bal = m_amount +amount
        print()
        print('Total Amount is : ',bal)
    else:
        print('Try Again')


def withdraw():
    if login() == 'yes':
        print()
        print('Welcome to Withdraw Section ..')
        amount = float(input('Enter amount to withdraw : '))
        m_amount = 5000
        bal = m_amount - amount
        print()
        print('Balance Amount is : ',bal)
    else:
        print('Try Again')


l1 = ['Deposite : d1','Withdraw : w1']
print('Welcome to Python  Bank ..')
print()
print('Services are : ',l1)
print()
v1 = input('Select your service option : ')
if v1 == 'd1':
    deposite()
elif v1 == 'w1':
    withdraw()    
else:
    print('Service not available..')




