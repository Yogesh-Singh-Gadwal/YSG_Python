# String
# ==, !=

user = 'micky'
phone = '99887766'
pwd = 'p123'
email = 'm@gmail.com'

v1 = input('Enter user name : ')
v2 = input('Enter user password : ')

if (user == v1 or phone == v1 or email == v1 ) and pwd == v2:  
    print('Login Success')
else:
    print('Login Failed')
    