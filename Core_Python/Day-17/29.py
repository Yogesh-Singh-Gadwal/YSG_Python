# function

def m1():
    try:
        a = int(input('Enter user value : '))
    except ValueError as ve:
        print('Exception : ',ve)
    try:
        print(10/a)
    except  UnboundLocalError as ue:
        print('Exception : ',ue)   
    print('Micky ---1 ')

try:
    m1()
except ZeroDivisionError as e:
    print('Exception name is : ',e)
else:
    print('Else.....')

print('Rest of the code....')


