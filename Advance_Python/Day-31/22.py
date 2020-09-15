import threading
import time


def m1():
    print(threading.currentThread().getName())

def m2():
    print(threading.currentThread().getName())

t1 = threading.Timer(5,m1)
t2 = threading.Thread(target=m2,name="Micky")

t1.start()
t2.start()

