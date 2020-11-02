#Converting space-delimiter records in csv format & writing into file
rec1 = '1234 John 10000 m US'
rec2 = '5678 Samantha 20000 f UK'

L1 = rec1.split()           #L1 = ['1234', 'John', '10000', 'm', 'US']
print(L1)
r1 = ','.join(L1) + '\n'    #'1234,John,10000,m,US\n'

                            #'1234 John 10000 m US'.replace(' ',',') + '\n'

L2 = rec2.split()
print(L2)
r2 = ','.join(L2)

header = "empid,empname,sal,gender,loc\n"


f = open("Micky.txt",'w')
f.write(header)
f.write(r1)
f.write(r2)
f.close()

