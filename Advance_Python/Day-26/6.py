# without inheritance

class GF():
    a = 10
    b = 20

class F():
    a = 10
    b = 20
    c = 30
    d = 40

class C():
    a = 10
    b = 20
    c = 30
    d = 50
    e = 60
    f = 70

print('GrandFather....')
gg = GF()
print(gg.a)
print(gg.b)

print()

print('Father....')
f = F()
print(f.a)
print(f.b)
print(f.c)
print(f.d)

print()

print('Child......')
c = C()
print(c.a)
print(c.b)
print(c.c)
print(c.d)
print(c.e)
print(c.f)


