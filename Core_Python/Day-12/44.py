# String

# split lines

v1 = '''Hi this is micky
i love my country
i stay in hyd
i enjoy lot '''


v2 = v1.splitlines()
print(v2)
print()
a = 1
for x in v2:
    print('Line : ',a,' : ',x)
    a +=1

