import threading

# functions

def m1():
    print('Micky...')

def m2():
    print('Akira....')

t1 = threading.Thread(target=m1)
t2 = threading.Thread(target=m2)

t1.start()
t2.start()
print(t1)
print(t2)



