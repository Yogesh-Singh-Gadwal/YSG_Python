# list 


l1 = ['ijk','qrstu','abcedf','lmno','gh']

# sort 
def size(l1):
    return len(l1)
size(l1)

l1.sort(key=size)
print('Result is : ',l1)


