# tuple

t1 = ('a',['b','c','d'],'e',['f','g','h'])

print(type(t1))
print('Value is : ',t1)
print()

t1[1][1] = 'z'
print('Value is : ',t1)

print()
t1[1][2] = 'micky'
print('Value is : ',t1)

print()

del t1[3][1]
print('Value is : ',t1)

print()
print()


del t1                     # NameError: name 't1' is not defined
print('Value is : ',t1)


