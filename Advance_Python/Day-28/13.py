# polymorphism

class Splander():
    def speed(self):
        print('Avg speed is 40 km/hr')


class Pulser():
    def speed(self):
        print('Avg speed is 55 km/hr')


def bike(status):
    status.speed()

s = Splander()
p = Pulser()

v1 = input('Enter your bike code : ')

if v1 == 's':
    bike(s)
elif v1 == 'p':
    bike(p)
else:
    print('Stock is not avaialable...')



