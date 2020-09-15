# 
import threading
import time

def m1():    
    time.sleep(1)
    print(threading.currentThread().getName())


for x in range(4):  # 0,1,2,3
    t1 = threading.Thread(target=m1)
    t1.start()
   



