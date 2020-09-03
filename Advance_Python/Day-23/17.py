# Class & Object

class Employee():
    a = 10
    b = 20
    # method
    def m1(self):
        print('Sum of value is : ',(self.a+self.b))

# 1st Object
e1 = Employee()

# 2nd Object
e2 = Employee()

# 3rd Object
e3 = Employee()

print('Object -1 Id : ',id(e1))
print()
print('Object -2 Id : ',id(e2))
print()
print('Object -3 Id : ',id(e3))

