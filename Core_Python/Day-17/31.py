# Exception

try:
    print('Connection established....')
    a = int(input('Enter user value : '))    
    int(10/a)
    print()
except:
    print()
    print('Opeartion is Failed...')
    print('Connection is Closed...')
else:
    print('Database operation is done ...')
    print('Connection is Closed...')

print('******* Thank you ********')

