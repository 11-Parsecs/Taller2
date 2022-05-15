##########################
#Escriba un programa que le pregunte al usuario por un input de la forma x^n para imprimir su derivada
##########################

Txt="Ingrese una función de la forma x^n: "
Txt2="La función debe tener la forma indicada."
Txt3="La derivada de {0} es {1}x^{2}."

Str=input(Txt)
Lst=list(Str)

A=Str.split("^") #Separa el string en el signo ^

if A[0]=="x": #Comprueba que el string ingresado tenga la forma requerida
    try:
        print(Txt3.format(Str,A[1],eval(A[1])-1)) #Imprime la derivada
    except:
        print(Txt2)
else:
    print(Txt2)