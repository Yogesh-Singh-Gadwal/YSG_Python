import threading
import time
# functions

def m1():
    time.sleep(3)
    print('Micky...')

def m2():
    time.sleep(2)
    print('Akira....')

t1 = threading.Thread(target=m1)
t2 = threading.Thread(target=m2)

t1.start()
t2.start()





