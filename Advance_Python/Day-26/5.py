# inheritance

class A(object):
    pass

class B(A):
    pass

a = A()
b = B()

print(issubclass(A,object))
print(issubclass(object,A))
print()

print(issubclass(B,A))
print(issubclass(A,B))

print()

print(issubclass(A,object))
print(issubclass(B,object))


