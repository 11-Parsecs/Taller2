Txt="Ingrese una función de la forma x^n: "
Txt2="La función debe tener la forma indicada."
Txt3="La derivada de {0} es {1}x^{2}."

Str=input(Txt)
Lst=list(Str)

A=Str.split("^")

if A[0]=="x":
    try:
        print(Txt3.format(Str,A[1],eval(A[1])-1))
    except:
        print(Txt2)
else:
    print(Txt2)