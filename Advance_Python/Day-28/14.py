# polymorphism
class Indian_Prodcuts():
    def oil(self):
        print('Cost of Oil is : 100 Rs')

    def shirt(self):
        print('Cost of Shirt is : 1200 Rs')  

    def pant(self):
        print('Cost of Pant is : 1800 Rs')   


class American_Prodcuts():
    def oil(self):
        print('Cost of Oil is : 5 $')

    def shirt(self):
        print('Cost of Shirt is : 15 $')  

    def pant(self):
        print('Cost of Pant is : 21 $ Rs')   


def product_Status(status):
    status.oil()
    status.shirt()
    status.pant()


i = Indian_Prodcuts()
a = American_Prodcuts()

v1 = input('Enter your product status code  : ')

if v1 == 'i':
    product_Status(i)
elif v1 == 'a':
    product_Status(a)
else:
    print('Stock is not avaialable...')

