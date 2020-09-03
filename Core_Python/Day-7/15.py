# Python

# less 40 failed 
# 40 but less 60 = 2nd 
# 60 but 80 = first
# 80 less 90 = topper
# 90 and less thn equal to 100 they are star ranker

score = int(input('Enter user Score : '))

if score < 40:
    print('Result is : Failed')
elif score >=40 and score <= 59:
    print('Second division')
elif score >=60 and score <= 79:
    print('First division')
elif score >=80 and score <= 89:
    print('Topper')
elif score >=90 and score <= 100:
    print('Star Ranker')
else:
    print('Need to check paper again')
        


        
