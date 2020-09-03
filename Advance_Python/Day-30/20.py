# # Encapsulation

class Score():
    def __init__(self):
        self.a = 123
        self._b = 456
        self.__c = 789

ss = Score()
print(ss.a)
print(ss._b)
print(ss.__c)  # AttributeError: 'Score' object has no attribute '__c'

