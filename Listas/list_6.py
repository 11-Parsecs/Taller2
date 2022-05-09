Loop=[]

for i in range(0,50):
    Loop.append(i)

print(Loop,end="\n\n")

#######################

Loop2=[]

for i in range(1,51):
    Loop2.append(i**2)
    
print(Loop2,end="\n\n")

#######################

Loop3=[]
n=0

for i in "abcdefghijklmnopqrstuvwxyz":
    n+=1
    Loop3.append(i*n)
    
print(Loop3)

