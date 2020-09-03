# list inside another list 

l1 = [1,2,3,4,5,6,7,8,9]
print('Value is : ',l1)

l2 = [10,11,12,13,14,15,16,17,18,19,20]

for x in range(len(l2)):
    l1.append(l2[x])

print('Value is : ',l1)    
