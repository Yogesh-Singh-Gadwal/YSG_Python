# nested loop

# country 
country = ['India','USA','JAPAN','UK']
students = ['Akash','Harish','Madhavi','Yogesh']

a =  0
while a < len(country):
    print('Country : ',country[a])
    print()
    b = 0
    while b < len(students):
        print(' '* 10,' Students : ',students[b])
        b +=1 
    a +=1
    print()

print('Loop Ends ....') 

