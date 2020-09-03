# List 

l1 = ['Rahul','Srinivas','Jay','Rahul','Mohit','Srinivas','Harsha']

print(l1)
print(type(l1))

print()

# converting list into set

s1 = set(l1)
print(s1)
print(type(s1))

print()

l1 = list(s1)
l1.sort()

print('Final Result is : ',l1)


