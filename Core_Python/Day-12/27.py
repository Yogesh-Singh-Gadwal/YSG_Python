# String
# in , not in 

# lower 

l1 = ['akash','vijay','harish','prasanna','sajid','madhavi','yogesh']

v1 = input('Enter user name : ').lower()

if v1 in l1:
    print(v1.capitalize(),', Yes Record is present')
else:
    print('Record is not find')

