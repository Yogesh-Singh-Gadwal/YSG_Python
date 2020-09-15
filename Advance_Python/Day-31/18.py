# 
import threading
import time
#('one',)

def m1(v1):
    time.sleep(2)
    print(threading.currentThread().getName(),' Name is : ',v1)

def m2(v2):
    time.sleep(2)
    print(threading.currentThread().getName(),' Name is : ',v2)

def m3(v3):
    time.sleep(2)
    print(threading.currentThread().getName(),' Name is : ',v3)


for x in range(4):
    t1 = threading.Thread(target=m1, args=('Micky --> ',))
    t1.start()
    t2 = threading.Thread(target=m2, args=('Akira -->',))
    t2.start()
    t3 = threading.Thread(target=m3, args=('Disney -->',))
    t3.start()


    
