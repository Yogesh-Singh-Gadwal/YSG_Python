import time

f = open("emp.txt","r")
print('Cursor position : ',f.tell())
print()
print(f.readline())
print()
time.sleep(3)

print('Cursor position : ',f.tell())
print()
time.sleep(3)

print('Read Value is : ',f.read(8))
print()
time.sleep(3)
print('Cursor position : ',f.tell())

