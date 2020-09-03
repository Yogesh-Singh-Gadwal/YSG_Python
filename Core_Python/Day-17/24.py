# exception

try:
    a = int(input('Enter user value : '))
    print(10/a)
    su = 0
    while(True):
        su  = su+1
        print('Micky : ',su)
except BaseException as e:
    print('Exception due to : ',e)

print('Rest of the code....') 

