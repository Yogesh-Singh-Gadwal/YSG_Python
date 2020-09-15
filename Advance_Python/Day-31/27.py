import threading 
import time

def m1():
    for x in range(1, 5):
        print('Thread Name is : ',threading.currentThread().getName(),' count : ',x)
        time.sleep(1)


t1 = threading.Thread(target=m1, name='Micky')
t1.start()





