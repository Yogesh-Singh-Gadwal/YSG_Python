# const
class Status():
    # const
    def __init__(self,name,phone,email,add,vid):
        self.name = name
        self.phone = phone 
        self.email = email
        self.add = add
        self.vid =  vid

    # getters method
    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email        
    
    def getAdd(self):
        return self.add

    def getVoterId(self):
        return self.vid



ee = Status('Micky',99887766,'m@gmail.com','Kphb-5',123456)

print(ee.getName())
print(ee.getAdd())
print(ee.getEmail())

print()


ee = Status('Sumit',99887766,'s@gmail.com','Kphb-7',123456)

print(ee.getName())
print(ee.getPhone())


print()


ee = Status('Jaya',99887766,'j@gmail.com','Kphb-7',123456)

print(ee.getEmail())
print(ee.getVoterId())



