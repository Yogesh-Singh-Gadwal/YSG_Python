# inheritance 

class Myclass1(object):
    # class variables
    a = 10
    b = 20

class Myclass2(Myclass1):
    pass

print(dir(Myclass1))
print()

print(dir(Myclass2))
print()


