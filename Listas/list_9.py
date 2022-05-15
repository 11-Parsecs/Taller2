##########################
#Encuentre totas las probabilidades con su porcentaje al sumar el valor que dan dos dados al ser lanzados.
##########################

from random import randint

N=1000000 #Número de veces que se lanzaron los dados
Count=[]

for n in range(1,N+1):
    A=randint(1,6)
    B=randint(1,6)
    Count.append(A+B)
    
for i in range(2,13):
    print(str(i)+":",str(Count.count(i)*100/N)+"%")