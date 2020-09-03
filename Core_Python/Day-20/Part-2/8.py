# tuple
# Tuple objects are immutable.

# list 
l1 = ['a','b','c']
print('Before : ',l1)
l1.append('d')
print('After : ',l1)

print()

# tuple 
l1 = ('a','b','c')
print('Before : ',l1)
l1.append('d')            # AttributeError: 'tuple' object has no attribute 'append'
print('After : ',l1)
