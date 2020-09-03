# loop 
# result

name = ['Aakash','Harish','Madhavi','Prasanna']
country = ['USA','UK','JAPAN','HONG KONG']

a = 0
for x in country : 
    print('Country : ',x)
    for x in range(0,a+1) : 
        print(' '*10,'Name : ',name[x])               
    print()
    a += 1 



'''

a = 0
for x in range(4):
    for x in range(0,a+1):
        print(x)
    a +=1
    print()
'''    