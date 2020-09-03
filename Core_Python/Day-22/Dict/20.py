# dict
import time
d1 = {
       "a":"micky",
       "b":"akira",
       "c":"rahul"
}

print(d1)
print(type(d1))
print()

v1 = d1.copy()
print(v1)
print(type(v1))

print()

d1['b'] = 'Harry'

print('D1 Value is : ',d1)
print(id(d1))
print('V1 Value is : ',v1)
print(id(v1))
