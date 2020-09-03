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
    print()
    if v2 == 'internet data':
        pass
    elif v2 == 'top up':
        pass
    elif v2 == 'recharge':
        l2 = [10,30,50,75,1000]
        print('Rechrage Avalilable are : ',l2)
        v3 = input('Enter your Recharge option : ')
        print(v3)
    elif v2 == 'tv':
        pass
    elif v2 == 'live music':
        pass
    else:
        print('Service is not valid')
else:
    print()
    print('****** Thank you for your Visit ******')
