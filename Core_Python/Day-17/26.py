# parent to child   Invalid
# exception

try:
    a = int(input('Enter user value : '))
    print(10/a)
except Exception as e:
    print('Exception due to : ',e)
except ZeroDivisionError as e:
    print('Exception due to : ',e)

print('Rest of the code...')


   

