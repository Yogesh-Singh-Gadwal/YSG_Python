import time

def m1():
    print('Method-1 is executing...')
    time.sleep(2)
    print('Micky---1')
    time.sleep(2)
    print('Method-1 execution is completed...')

def m2():
    print('Method-2 is executing...')
    time.sleep(2)
    print('Micky---2')
    time.sleep(2)
    print('Method-2 execution is completed...')

print()
m1()

time.sleep(2)

print()
m2()

