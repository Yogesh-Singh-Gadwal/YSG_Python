import threading
import time

def status():
    print('Micky-1')
    print('Thread Name is : ',threading.currentThread().getName())
    time.sleep(1)


t1 = threading.Thread(target=status)
t1.start()

time.sleep(5)
print('Active threads are : ',threading.active_count())

