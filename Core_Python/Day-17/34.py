# Exception

try:
    print('Connection established....')
    a = int(input('Enter user value : '))    
    int(10/a)
    print()
except:
    print()
    print('Opeartion is Failed...')   
else:
    print('Database operation is done ...')    
finally:
    print()
    print('Connection is Closed...')

