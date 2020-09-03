# function calling
# inner function calling
def a1():
    print('Function -1')
    b1()

def b1():
    print('Function -2')
    c1()

def c1():
    print('Function -3')
    d1()

def d1():
    print('Function -4')
    e1()

def e1():
    print('Function -5')

a1()
