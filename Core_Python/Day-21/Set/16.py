# Set
import time
s1 = {'a','b','c','d'}

print('S1 is : ',s1)
s1.remove('b')

print('S1 is : ',s1)

time.sleep(2)
print()

s1.remove('b')
print('S1 is : ',s1)  # KeyError: 'b'





