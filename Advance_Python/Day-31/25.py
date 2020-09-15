import threading
import time

def m1():
    print('Micky-1')
    print('Thread Name is : ',threading.currentThread().getName())
    print()
    time.sleep(7)

def m2():
    print('Micky-2')
    print('Thread Name is : ',threading.currentThread().getName())
    print()
    time.sleep(7)

def m3():
    print('Micky-3')
    print('Thread Name is : ',threading.currentThread().getName())
    print()
    time.sleep(3)

print()
print('Active threads are : ',threading.active_count())
time.sleep(2)
print()

t1 = threading.Thread(target=m1)
t1.start()
print('Active threads are : ',threading.active_count())
time.sleep(2)


t2 = threading.Thread(target=m2)
t2.start()
print('Active threads are : ',threading.active_count())
time.sleep(2)


t3 = threading.Thread(target=m3)
t3.start()
print('Active threads are : ',threading.active_count())
time.sleep(2)

print()
print('Active threads are : ',threading.active_count())

print()
time.sleep(10)
print('Active threads are : ',threading.active_count())
