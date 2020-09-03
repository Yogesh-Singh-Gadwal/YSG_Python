# dict
a = ("Rahul","Mahesh","shoaib")

b = ('Icici','SBI')

#res = dict.fromkeys(a,b)

#print('Result is : ',res)

#  ------------
'''
z = 0
for x in a:
    for y in b:
        print(x,end=' ')
        print(b[z])
        z +=1
        break
    print()
'''

for x in range(len(a)):
    print('A Value is : ',a[x])
    for y in range(len(b)):
        if x == y:
            print('B Value is : ',b[x])
        else:
            print('B Value is : ',None)    
        break
    print()    

