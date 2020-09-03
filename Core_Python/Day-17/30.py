# Exception

def m1():
    n = int(input('Enter usr value : '))
    print(10/n)

def m2():
    print('a'+10) 

try:
    m1()
    m2()
except Exception as ae:
    print('Exception due to : ',ae)
else:
    print('Else..............')

print('Rest of the code....')

