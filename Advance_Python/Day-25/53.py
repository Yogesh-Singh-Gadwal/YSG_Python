# class 

import time
class Myclass():
    def __del__(self):
        print('Object is deleted...')


c1 = Myclass()
print(c1)
del c1

time.sleep(3)
print()

c2 = Myclass()
print(c2)
del c2

time.sleep(3)
print()

c3 = Myclass()
print(c3)
del c3
