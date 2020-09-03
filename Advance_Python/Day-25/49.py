# const
from time import sleep
class Status():
    # setters method
    def setName(self,name):
        self.name = name
        
    def setPhone(self,phone):
        self.phone = phone

    def setEmail(self,email):
        self.email = email

    def setAdd(self,add):
        self.add = add 

    def setVoterId(self,vid):
        self.vid = vid    

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



ee = Status()
v1 = input('Enter user name : ')
ee.setName(v1)
ee.setAdd('KPHB-5')
print('Result is : ',ee.getName())


print()
sleep(3)

ee = Status()
ee.setName('Akira')
ee.setPhone(99887766)

print(ee.getPhone())


print()
sleep(3)

ee = Status()
ee.setName('Jaya')
ee.setEmail('j@gmail.com')
ee.setVoterId(12345)
print(ee.getName())
print(ee.getEmail())
print(ee.getVoterId())



