# 
import threading
import time

def m1():
    for x in range(4):
        time.sleep(2)
        print(threading.currentThread().getName())
        print()
def m2():
    for x in range(4):
        time.sleep(2)
        print(threading.currentThread().getName())
        print()

def m3():
    for x in range(4):
        time.sleep(2)
        print(threading.currentThread().getName())
        print()


t1 = threading.Thread(target=m1)
t2 = threading.Thread(target=m2)
t3 = threading.Thread(target=m3)
t1.start()
t2.start()
t3.start()


