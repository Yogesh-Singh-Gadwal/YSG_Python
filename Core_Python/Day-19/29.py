# list
# removing Sec duplicate value only
l1 = ['Aakash','Micky','Harish','Kishan','Micky','Pavan','Harish','Micky','Pavan','Harish']

print('Value are : ',l1)
print()
v1 = input('Enter user value : ')
a = 0
l2 = []
for x in l1:    
    if x not in l2:
        l2.append(x)
    else:
        if x != v1:
           l2.append(x) 
        elif x == v1:
            a+=1
            if a == 1:
                continue
            else:
                l2.append(x) 
        

print('Result is : ',l2)
