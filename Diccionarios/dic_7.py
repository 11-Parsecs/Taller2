Txt="Los tres números más comunes son {0}, {1} y {2}."

N=10

from random import randint
Mat=[]
for i in range(5):
    Row=[]
    for j in range(5):
        Row.append(randint(0,N))
    Mat.append(Row)
print(Mat)

Nums={}

for n in range(N+1):
    v=0
    for L in Mat:
        v+=L.count(n)
    Nums[n]=v

print(Nums)

Maxs=[]

for i in range(3):
    d=max(Nums,key=Nums.get)
    del Nums[d]
    Maxs.append(d)

print(Txt.format(*Maxs))