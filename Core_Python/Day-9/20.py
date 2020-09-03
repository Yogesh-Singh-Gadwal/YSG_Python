# loop 
# result

name = ['Aakash','Harish','Madhavi','Prasanna']
country = ['USA','UK','JAPAN','HONG KONG']

a = 0
for x in country : 
    print('Country : ',x)
    for x in name : 
        print(' '*10,'Name : ',name[a])
        a += 1
        break
    print()
