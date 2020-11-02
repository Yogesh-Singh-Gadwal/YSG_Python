# Pickle means converting into binary format
import pickle

d = {}
d['id'] = 12
d['name'] = 'Obama'
d['salary'] = 900000.0  

print(d)               # d={'id':12,'name':'Obama','salary':900000.0}


input('Enter to cont...')


#Pickling
bdata = pickle.dumps(d)

print(bdata)
print("-"*40)


input('Enter to cont...')
f = open('employee.pickle','wb')
f.write(bdata)
f.close()

