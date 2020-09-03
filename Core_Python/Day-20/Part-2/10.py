# tuple
# Tuple objects are immutable.

# list 
l1 = ['a','b','c']
print('Before : ',l1)
l1[1] = 'z'
print('After : ',l1)

print()

# tuple 
l1 = ('a','b','c')
print('Before : ',l1)
l1[1] = 'z'            # TypeError: 'tuple' object does not support item assignment
print('After : ',l1) 

