# nested if with else
from time import sleep 

print()
print('Welcome to Python customer care center ')
print()
sleep(2)
l1 = ['Internet data','Top Up','Recharge','Tv','Live Music']

v1 = input('Are you looking for some service : ')
if v1 == 'yes':
    print()
    print('Welcome to Service option ')
    print()
    sleep(2)
    print('Available service are : ',l1)
    v2 = input('Select your Service Code : ')
    print(v2)
else:
    print()
    print('****** Thank you for your Visit ******')

   

