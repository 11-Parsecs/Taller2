# 3x+4y -> 3*x+4*y
# 3(x+5) -> 3*(x+5)

##########################
#Escriba un programa que pida una expresión algebraica para insertar el símbolo de multiplicación donde es apropiado
#Ejemplo: 3x+4y -> 3*x+4*y
##########################

Txt1="Ingrese una expresión algebraica: "

A=input(Txt1)
B=list(A)
C=list(A)
N=[]

p=0
d=0
n_i=A[0] #n es el string actual y n_i es el string anterior

for n in C:
    
    if not n.isdigit() and not n in "*()/^+-" and n_i not in "*(/^+-" or n.isdigit() and n_i==")":
        B.insert(p+d,"*") #Compara los string para saber si se ingresa un *
        d+=1

    n_i=n
    p+=1

C="".join(B)
C.replace("^","**") #Como extra, reemplaza los ^ por **
print(C)