# File
import time

f = open("emp.txt","r")

f.seek(40)
print('Cursor position : ',f.tell())
print(f.readline())
print('Cursor position : ',f.tell())
print()
time.sleep(2)

f.seek(10)
print('Cursor position : ',f.tell())
print(f.readline())
print('Cursor position : ',f.tell())
print()
time.sleep(2)

print(f.readline())
print('Cursor position : ',f.tell())
