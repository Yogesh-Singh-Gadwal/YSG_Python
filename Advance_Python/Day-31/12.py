import threading
import time
# functions

def m1(v1):
    for x in range(5):
        time.sleep(1)
        print('Micky...')

def m2(v2):
    for x in range(5):
        time.sleep(1)
        print('Disney....')

t1 = threading.Thread(target=m1, args=('**',))
t2 = threading.Thread(target=m2, args=('$$',))

t1.start()
t2.start()





