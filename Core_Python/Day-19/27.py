# list
# remove using duplicate
l1 = ['Aakash','Micky','Harish','Kishan','Micky','Pavan','Harish','Micky','Pavan']


#l1.remove('Micky')
#print('Result is : ',l1)
print('Value are : ',l1)
print()
v1 = input('Enter user value : ')
co = l1.count(v1)

for x in range(co):
    l1.remove(v1)
print('Result is : ',l1)
