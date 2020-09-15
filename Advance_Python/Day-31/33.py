import threading
import time

class Myone(threading.Thread):
    def __init__(self,name,count):
        threading.Thread.__init__(self)
        self.threadID = count
        self.name = name 
        self.counter = count
        
    def run(self):
        print("Starting value : ",self.name)
        print()
        m1(self.name,self.counter)
        time.sleep(3)
        print()
        print("End value is :",self.name)


def m1(name ,count):
    print('Micky-1')
    time.sleep(2)
    print('Disney-1')

t = Myone('IndiaThread-1',100)
t.start()

