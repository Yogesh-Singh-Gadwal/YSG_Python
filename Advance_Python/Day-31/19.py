# 
import threading
import time


def m1():
    time.sleep(2)
    print('Name is : ',threading.currentThread().getName())

def m2():
    time.sleep(2)
    print('Name is : ',threading.currentThread().getName())



t1 = threading.Thread(target=m1, name='Micky')
t1.start()
t2 = threading.Thread(target=m2, name='Mouse')
t2.start()



    



