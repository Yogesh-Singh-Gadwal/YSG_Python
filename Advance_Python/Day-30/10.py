# Encapsulation

class Myclass():
    # method(Private)
    def __m1(self):
        print('Parent Method...')


c = Myclass()
c.__m1()      # AttributeError: 'Myclass' object has no attribute '__m1'






