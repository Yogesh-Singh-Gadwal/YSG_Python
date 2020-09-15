import threading 
import time

def m1():
    for x in range(1, 4):
        print('Thread Name is : ',threading.currentThread().getName(),' count : ',x)
        time.sleep(1)

def m2():
    for x in range(1, 9):
        print('Thread Name is : ',threading.currentThread().getName(),' count : ',x)
        time.sleep(1)




t1 = threading.Thread(target=m1, name='Micky')
t2 = threading.Thread(target=m2, name='Computer')


t1.start()

t2.setDaemon(True)
t2.start()


