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

del d1['b']

print(d1)

time.sleep(3)

del d1
print(d1)  # NameError: name 'd1' is not defined



