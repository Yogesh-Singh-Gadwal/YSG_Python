# dict

d1 = {
       "a":"micky",
       "b":"akira",
       "c":"rahul"
}

print(d1)
print(type(d1))
print()

# loop
l1 = []
for x in d1:
    l1.append(x)
print('Which key Record : ',l1, end='  ')    
v1 = input('Enter key  : ')
print()
for x in d1:
    if x == v1:
        print('Key : ',x,'   -->   Values  :',d1[x])    # Key and Values

    

