# Const

import time

class Myclass():
    pass

c = Myclass()
print(c)

time.sleep(3)
print()
print(c)

print()
del c

time.sleep(3)
print()
print(c)  # NameError: name 'c' is not defined


