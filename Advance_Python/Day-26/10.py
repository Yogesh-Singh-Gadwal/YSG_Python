# with inheritance

class A():
    a = 10
    b = 20

class B(A):
    c = 30
    d = 40
     
class C(B):
    e = 60
    f = 70
    print('Value of A is : ',A.a)
    print('Value of B is : ',A.b)
    print('Value of C is : ',B.c)
    print('Value of D is : ',B.d)
    print('Value of E is : ',e)
    print('Value of F is : ',f)


print()
print()


cc = C()
#print(dir(C))
print('Value of A is : ',cc.a)
print('Value of B is : ',cc.b)
print('Value of C is : ',cc.c)
print('Value of D is : ',cc.d)
print('Value of E is : ',cc.e)
print('Value of F is : ',cc.f)

