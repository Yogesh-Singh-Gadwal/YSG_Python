# function

def m1():
    a = int(input('Enter user value : '))
    print(10/a)
    print('Micky ---1 ')

try:
    m1()
except Exception as e:
    print('Exception name is : ',e)
else:
    print('Else.....')

print('Rest of the code....')


