# list
# remove using duplicate
l1 = ['Aakash','Micky','Harish','Kishan','Micky','Pavan','Harish','Micky','Pavan']

print('Value are : ',l1)
print()
v1 = input('Enter user value : ')

l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
    else:
        if x != v1:
           l2.append(x)   

print('Result is : ',l2)



