# List
# copy

l1 = ['Aakash','Harish','Kishan','Pavan','Sajid','Madhavi','Vivek','Yogesh']
print('Value of L1 : ',l1)

l2 = l1.copy() 

print('Value of L2 : ',l2) 
print('Id of L1 : ',id(l1))
print('Id of L2 : ',id(l2))
print()
l1.append('50')
print('Value of L1 : ',l1)
print('Value of L2 : ',l2)
