# const

class Status():
    # const
    def __init__(self,name,phone,email,add,vid):
        self.name = name
        self.phone = phone 
        self.email = email
        self.add = add
        self.vid =  vid

    def mystatus(self):
        print('Name : ',self.name) 
        print('Phone : ',self.phone)
        print('Email : ',self.email)
        print('Address : ',self.add)
        print('Voter Id : ',self.vid)

ss =  Status('micky','m@gmail.com','Kphb-5')


