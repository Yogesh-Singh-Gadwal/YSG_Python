# Encapsulation

class Subject():
    def __init__(self):
        self.__math()

    def science(self):
        print('Science..')

    # private method
    def __math(self):
        print('Math')

ss = Subject()
ss.science()

