# File

f = open("emp.txt","r")

s = f.read()
print(len(s))
print(type(s))
print(s)
print('Cursor position : ',f.tell())

input('Type to contu....')


# ending of line space is also include check file
print(f.seek(len(s)+20))
print(f.readline())
print('Cursor position : ',f.tell())

