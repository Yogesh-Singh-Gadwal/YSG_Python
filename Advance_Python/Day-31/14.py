# 
import threading
import time

def m1():
    time.sleep(2)
    print(threading.currentThread().getName())

def m2():
    time.sleep(2)
    print(threading.currentThread().getName())

def m3():
    time.sleep(2)
    print(threading.currentThread().getName())


t1 = threading.Thread(target=m1)
t2 = threading.Thread(target=m2)
t3 = threading.Thread(target=m3)
t1.start()
t2.start()
t3.start()


