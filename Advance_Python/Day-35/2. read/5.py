# File Handling

myfile = open('myone.txt',"rt")
# print(myfile.readlines())

res = myfile.readlines()
#print(res)
l2 = []
for x in res:
    l2.append(x.strip())


print('Final Result is : ',l2)



