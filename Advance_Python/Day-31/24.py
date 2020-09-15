import threading
import time

def m1():
    print('Micky-1')
    print('Thread Name is : ',threading.currentThread().getName())
    print()
    time.sleep(1)

def m2():
    print('Micky-2')
    print('Thread Name is : ',threading.currentThread().getName())
    print()
    time.sleep(1)

def m3():
    print('Micky-3')
    print('Thread Name is : ',threading.currentThread().getName())
    print()
    time.sleep(1)


t1 = threading.Thread(target=m1)
t1.start()

t2 = threading.Thread(target=m2)
t2.start()

t3 = threading.Thread(target=m3)
t3.start()

#time.sleep(2)

print('Active threads are : ',threading.active_count())

