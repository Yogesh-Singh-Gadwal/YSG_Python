import threading
import time

def m1():
    print('Micky-1')    
    print()
    time.sleep(4)

def m2():
    print('Micky-2')
    print()
    time.sleep(4)

def m3():
    print('Micky-3')    
    print()
    time.sleep(4)


t1 = threading.Thread(target=m1)
t1.start()

t2 = threading.Thread(target=m2)
t2.start()

t3 = threading.Thread(target=m3)
t3.start()

print()
print('Active threads are : ',threading.active_count())
print()
time.sleep(2) 
print()
for thread in threading.enumerate():
    print('Active threads Names are : %s'%thread.getName())

print()
print()
time.sleep(6) 
print('Active threads are : ',threading.active_count())
print()
for thread in threading.enumerate():
    print('Active threads Names are : %s'%thread.getName())

