# Exception Handling
# normal termination
try:
    print('Micky-1')
    print('Micky-2')
    v1 = int(input('Enter user value : '))
    print(10/v1)
except ZeroDivisionError as z:
    print('Exception raised due to : ',z)    
except:
    print('Default')    
print()
print('Rest of the code...')

