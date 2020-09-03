# Test

class Test():
    def __init__(self):
        self.variable = 'Old'
        self.result(self.variable)

    def result(self,var):
        var = 'New'    

res = Test()
print(res.variable)

