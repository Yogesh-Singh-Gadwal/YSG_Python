# File
import time
f = open("emp.txt","r")
print()
'''
print(f)
print()
print(f.read())


'''
print('Cursor position : ',f.tell())
time.sleep(3)

print(f.read(5))
time.sleep(3)

print('Cursor position : ',f.tell())
print()

print(len(str(f)))
