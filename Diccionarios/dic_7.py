##########################
#Cree una lista de números 5x5, luego escriba un progama que cree un diccionario,
#cuyas keys son los números y values la cantidad que aparecen, luego,
#imrpima los tres números más comunes.
##########################

Txt="Los tres números más comunes son {0}, {1} y {2}."

N=10 #Número máximo que saldrá en la matriz

from random import randint
Mat=[]
for i in range(5):
    Row=[]
    for j in range(5):
        Row.append(randint(0,N))
    Mat.append(Row) #Crea una lista 5x5 con valores aleatorios
print(Mat)

Nums={}

for n in range(N+1):
    v=0
    for L in Mat:
        v+=L.count(n)
    Nums[n]=v #Crea el diccionario con los números y la cantidad de veces que aparecen

print(Nums)

Maxs=[]

for i in range(3):
    d=max(Nums,key=Nums.get)
    del Nums[d]
    Maxs.append(d) #Crea la lista con los tres número que más se repiten.

print(Txt.format(*Maxs)) #Si dos valores aparecen la misma cantidad de veces, se mostrará el primero que sale de izqueirda a derecha