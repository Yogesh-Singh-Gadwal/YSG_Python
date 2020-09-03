# class 

import time
class Myclass():
    def __del__(self):
        print('Object is deleted...')



c1 = Myclass()
print(c1)
time.sleep(3)
del c1



