# Encapsulation

class Myclass():
    # class variable
    __a = 10
    b = 20
    print(__a)
    print(b)
    
print(dir(Myclass)) 
print()

class Child(Myclass):
      pass

print(dir(Child))    


 





