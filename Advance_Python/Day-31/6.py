import threading
import time

# logic
def m1():
    print('Micky-1')

# converting into thread
t1 = threading.Thread(target=m1)
print(t1)

# starting
t1.start()
print(t1)
print()
time.sleep(4)
print(t1)

