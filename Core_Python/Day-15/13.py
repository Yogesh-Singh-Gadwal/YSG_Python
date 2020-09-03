# function 
# normal funx

l1 = ['akash','micky','harish','prasanna','micky','sajid','madhavi','micky','yogesh']
l2 = []
def m1(l1):
    for x in l1:
        if x != 'micky':
            l2.append(x)
        else:
            pass

m1(l1)
print('Value is : ',l2)



# filter

l3 = ['akash','micky','harish','prasanna','micky','sajid','madhavi','micky','yogesh']

def m2(l3):
    if l3 != 'micky':
        return True
    else:
        return False

print('Result is : ',list(filter(m2,l3)))


# lambda + filter

l4 = ['akash','micky','harish','prasanna','micky','sajid','madhavi','micky','yogesh']
print('Final Result is : ',list(filter(lambda x : x != 'micky',l4)))




