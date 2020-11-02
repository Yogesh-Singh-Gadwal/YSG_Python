# python
import csv

# reading all csv data
with open('emp.csv') as file:
    data = csv.reader(file)
    for x in data:
        print(x)


print()
print()

# read particular column value
with open('emp.csv') as file:
    data = csv.reader(file)
    for x in data:
        #print(x[2])
        print(x[1],' ---- ',x[4])
        