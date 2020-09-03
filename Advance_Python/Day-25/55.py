# class 

import time
class Myclass():
    def __del__(self):
        print('Object is deleted...')

c1 = Myclass()
c2 = c1
c3 = c2
print(c1)
time.sleep(3)
del c1
print('First----')

time.sleep(3)

del c2
print('Sec----')

time.sleep(3)

del c3
print('Third----')


