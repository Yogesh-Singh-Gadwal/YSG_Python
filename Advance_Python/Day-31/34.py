import threading
import time

class Myone(threading.Thread):
    def m1(self):
        print('Micky-1 : ',threading.current_thread().getName())
        time.sleep(3)
        print('Disney-1 : ',threading.current_thread().getName())
        print()


t1 =  threading.Thread(target=Myone(name='THREAD-1').m1)
t1.start()

t2 =  threading.Thread(target=Myone(name='THREAD-2').m1)
t2.start()

t3 =  threading.Thread(target=Myone(name='THREAD-3').m1)
t3.start()


