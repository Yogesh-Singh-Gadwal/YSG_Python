# Class and object
class Myone():
    def m1(self):
        pass

m1 = Myone()
m2 = Myone()
m3 = m2

print(id(m1))
print()
print(id(m2))
print()
print(id(m3))

print()

print(m1 is m2)
print()
print(m2 is m3)

