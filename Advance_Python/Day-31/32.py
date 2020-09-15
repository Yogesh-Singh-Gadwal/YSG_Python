import threading
import time

class Myone(threading.Thread):
    def m1(self):
        print('Micky--1')
        time.sleep(3)
        print('Disney--1')

threading.Thread(target=Myone().m1).start()


