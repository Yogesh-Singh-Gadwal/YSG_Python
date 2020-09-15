# 
import threading
import time


def m1():
    time.sleep(2)
    print('Name is : ',threading.currentThread().getName())


t1 = threading.Thread(target=m1, name='Micky')
t1.start()

time.sleep(5)

t1 = threading.Thread(target=m1, name='Micky')
t1.start() 




