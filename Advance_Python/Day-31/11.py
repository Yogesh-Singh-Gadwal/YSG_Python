import threading
import time
# functions

def m1():
    for x in range(5):
        time.sleep(1)
        print('Micky...')

def m2():
    for x in range(5):
        time.sleep(1)
        print('Akira....')

t1 = threading.Thread(target=m1)
t2 = threading.Thread(target=m2)

t1.start()
t2.start()



