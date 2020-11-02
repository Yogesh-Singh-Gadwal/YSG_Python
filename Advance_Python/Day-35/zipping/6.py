import time

f = open("emp.txt","r")

print(f.read())

time.sleep(2)
f.close()
print()
print('File is closed....')
print()

time.sleep(5)
print('Reading file again...')
print()
time.sleep(3)
print(f.read())  # ValueError: I/O operation on closed file.

