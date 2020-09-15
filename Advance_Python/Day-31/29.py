# join
import threading
import time

def m1():
    for x in range(4):
        print('Micky - ',x)
        time.sleep(1)

def m2():
    for x in range(4):
        print('Disney - ',x)
        time.sleep(2)


t1 =  threading.Thread(target=m1)
t2 =  threading.Thread(target=m2)

t1.start()
t1.join()
t2.start()


