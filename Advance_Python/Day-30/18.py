# Encapsulation

class Subject():
    def __init__(self):
        pass

    def science(self):
        print('Science..')

    # private method
    def __math(self):
        print('Math')

ss = Subject()
ss.science()
ss.__math()  # AttributeError: 'Subject' object has no attribute '__math'


