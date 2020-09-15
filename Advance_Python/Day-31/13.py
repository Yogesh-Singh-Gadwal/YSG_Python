# 
import threading
import time

def m1():
    time.sleep(2)
    print(threading.currentThread().getName())

t1 = threading.Thread(target=m1)
t1.start()


