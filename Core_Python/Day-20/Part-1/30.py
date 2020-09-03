# list
# removing Sec duplicate value only
l1 = ['Aakash','Micky','Harish','Kishan','Micky','Pavan','Harish','Micky','Pavan','Harish']

print('Value are : ',l1)
print()
v1 = input('Enter user value : ')
a = 0
b = 0
l2 = []
for x in l1:
    if v1 == x:
        b +=1
        if not(b == 2):
            l2.append(x)
    else:
        l2.append(x)
        a+=1

print('Result is : ',l2)

