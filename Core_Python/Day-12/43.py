# String

# split

s1 = 'hi this is micky from india'
print(s1.split())

# or

s1 = 'hi,this,is,micky,from,india'
print(s1.split(','))

# or

s1 = 'Hi this is micky.I love my Country'
print(s1.split('.'))

s2 = s1.split('.')

for x in s2:
    print(x)

