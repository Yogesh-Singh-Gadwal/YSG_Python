# Encapsulation

# without

class Myclass():
    # class variable
    __a = 10

    print(__a)

c = Myclass()
print(c.__a) #AttributeError: 'Myclass' object has no attribute '__a'




