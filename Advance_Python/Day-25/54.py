# class 

import time
class Myclass():
    def __del__(self):
        print('Object is deleted...')



c1 = Myclass()
print(c1)
del c1

time.sleep(3)

print('Micky -1')

time.sleep(3)

print('Micky -2')


