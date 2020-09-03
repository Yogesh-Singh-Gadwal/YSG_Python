# String 

# 3. strip() method removes any whitespace from the beginning or the end

s1 = 'micky'
print(len(s1))

print()

s1 = '   micky   '
print(len(s1))
print()

s2 = s1.strip()
print(len(s2))
print(s2)
print()

s1 = '   micky   '
print(len(s1))
s2 = s1.lstrip()
print(len(s2))
print(s2)
