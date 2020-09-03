#  polymorphism
class Indian_Prodcuts():
    def country(self):
        print('India : ')
 
    def oil(self):
        print('Cost of Oil is : 100 Rs')

    def shirt(self):
        print('Cost of Shirt is : 1200 Rs')  

    def pant(self):
        print('Cost of Pant is : 1800 Rs')   


class American_Prodcuts():
    def country(self):
        print('USA : ')

    def oil(self):
        print('Cost of Oil is : 5 $')

    def shirt(self):
        print('Cost of Shirt is : 15 $')  

    def pant(self):
        print('Cost of Pant is : 21 $ Rs')   


def product_Status(status):
    status.country()
    print('--------')
    status.oil()
    status.shirt()
    status.pant()
    print();print()

#i = Indian_Prodcuts()
#a = American_Prodcuts()
print()

for product in [Indian_Prodcuts(),American_Prodcuts()]:
    product_Status(product)

    


