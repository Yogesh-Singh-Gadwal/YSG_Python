# Function

def m1():
    a = int(input('Enter user value-1 : '))
    b = int(input('Enter user value-2 : '))
    print('Sum of value is : ',a+b)

# Function

def m2():
    a = int(input('Enter user value-1 : '))
    b = int(input('Enter user value-2 : '))
    print('Sub of value is : ',a-b)

v1 = input('Select addition (+) or subtraction (-) : ')
print()
if v1 == '+':
    m1()
else:
    m2()
