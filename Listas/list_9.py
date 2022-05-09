from random import randint

Count=[]

for n in range(1,10001):
    A=randint(1,6)
    B=randint(1,6)
    Count.append(A+B)
    
for i in range(2,13):
    print(str(i)+":",str(Count.count(i)/100)+"%")



