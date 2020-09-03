# tuple
# Tuple objects are immutable.

# list 
l1 = ['a','b','c']
print('Before : ',l1)
l1.remove('b')
print('After : ',l1)

print()

# tuple 
l1 = ('a','b','c')
print('Before : ',l1)
l1.remove('b')           # AttributeError: 'tuple' object has no attribute 'remove'
print('After : ',l1) 

