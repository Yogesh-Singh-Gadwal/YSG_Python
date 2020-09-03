# exception

try:
    a = int(input('Enter user value : '))
    print(10/a)
except BaseException as e:
    print('Exception due to : ',e)
else:
    print('Else....')
print('Rest of the code....') 



