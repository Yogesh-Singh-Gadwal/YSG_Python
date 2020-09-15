import threading
import time

class Myone(threading.Thread):
    def m1(self):
        print('Micky-1 : ',threading.current_thread().getName())
        time.sleep(3)
        print('Disney-1 : ',threading.current_thread().getName())

    def m2(self):
        print('Micky-2 : ',threading.current_thread().getName())
        time.sleep(3)
        print('Disney-2 : ',threading.current_thread().getName())

    def m3(self):
        print('Micky-3 : ',threading.current_thread().getName())
        time.sleep(3)
        print('Disney-3 : ',threading.current_thread().getName())


t1 =  threading.Thread(target=Myone(name='THREAD-1').m1)
t1.start()

t2 =  threading.Thread(target=Myone(name='THREAD-2').m2)
t2.start()

t3 =  threading.Thread(target=Myone(name='THREAD-3').m3)
t3.start()
