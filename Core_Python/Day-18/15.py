# list
# count

l1 = ['Aakash','Micky','Harish','Kishan','Micky','Pavan','Harish','Micky','Pavan']
l2 = []
for x in range(len(l1)):
    if l1[x] in l2:
        continue
    else:
        l2.append(l1[x])
print()
for x in range(len(l2)):
    print(l2[x],' = ','Count value is : ',l1.count(l2[x]))
    