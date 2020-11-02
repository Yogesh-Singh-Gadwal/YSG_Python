#Unpickling

import pickle

f1 = open('employee.pickle','rb')
bs1 = f1.read()

print(bs1)

input('Enter .. ')


d1 = pickle.loads(bs1)

print(d1)
f1.close()


