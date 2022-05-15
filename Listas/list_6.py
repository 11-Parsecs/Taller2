##########################
#Cree una lista como dice cada enunciado:
#(a) Una lista con los enteros del 0 al 49
#(b) Una lista con todos los cuadrados de los enteros del 1 al 50
#(c) La lista ['a','bb','ccc','dddd', . . . ] que termina con 26 copias de la letra z
##########################

##############
#a)
##############

Loop=[]

for i in range(0,50):
    Loop.append(i)

print(Loop,end="\n\n")

##############
#b)
##############

Loop2=[]

for i in range(1,51):
    Loop2.append(i**2)
    
print(Loop2,end="\n\n")

##############
#c)
##############

Loop3=[]
n=0

for i in "abcdefghijklmnopqrstuvwxyz":
    n+=1
    Loop3.append(i*n) #En los string, la multiplicación lo duplica
    
print(Loop3)