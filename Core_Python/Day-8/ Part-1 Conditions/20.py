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
        print()
        if v3 == '10':
            print('*'*30)
            print()
            print('Recharge of 10  will give you : 7 Rs')
            print()
            print('*'*30)            
        elif v3 == '30':
            print('*'*30)
            print()
            print('Recharge of 30  will give you : 25 Rs')
            print()
            print('*'*30) 
        elif v3 == '50':
            print('*'*30)
            print()
            print('Recharge of 50  will give you : 46 Rs')
            print()
            print('*'*30) 
        elif v3 == '75':
            print('*'*30)
            print()
            print('Recharge of 75  will give you : 73 Rs')
            print()
            print('*'*30) 
        elif v3 == '1000':
            print('*'*30)
            print()
            print('Recharge of 1000  will give you : 1000 Rs')
            print()
            print('*'*30) 
        else:
            print('Recharge is not valid..')
    elif v2 == 'tv':
        pass
    elif v2 == 'live music':
        pass
    else:
        print('Service is not valid')
else:
    print()
    print('****** Thank you for your Visit ******')
