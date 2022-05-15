##########################
#(a) Escriba un programa que convierta números romanos en números ordinarios. 
#(b) Escriba un programa que convierta números ordinarios en números romanos.
##########################

Txt="Ingrese un número {}{} menor que 4000: "
Txt1="Eso no es un número {}."
Txt2="romano"
Txt3="arábigo"
Txt4="El número no es válido."
Txt5=" en mayúsculas"

Roman={"M":"1000","D":"500","C":"100","L":"50","X":"10","V":"5","I":"1"}

##############
#a)
##############

def Rom2Ara(Rom):

    """
    Convierte el número romano Rom en un número arábigo.

    ####################

    Rom: str
    Número en romano

    ####################

    Rom2Ara("XLIV")
    >>> 44
    """

    Inv=Rom[::-1] #Invierte el string del número romano para facilitar la función

    Ara=int(Roman[Inv[0]]) #Acumula las suma y resta de las letras del número romano para llegar a la solución

    for i,i1 in zip(Inv[1:],Inv[:len(Inv)]): #i es la posición actual e i1 es la posición anterior
        n_i=eval(Roman[i])
        n_i1=eval(Roman[i1])
        if n_i1>n_i:
            if n_i in [5,50,500]:
                Ara=Txt4
                break
            elif n_i1/10 != n_i and n_i1/5 != n_i: #Muestra como inválidos los números como ID
                Ara=Txt4
                break
            else:
                Ara-=n_i #Si la posición anterior es mayor se resta el número
        else:
            Ara+=n_i #Si la posición anterior es mayor se suma el número
    return Ara

In1=input(Txt.format(Txt2,Txt5))
try:
    Out1=Rom2Ara(In1)
    print(Out1)
except:
    print(Txt1.format(Txt2)) #Si la función falla, el número no es romano

##############
#b)
##############

def Ara2Rom(Ara):

    """
    Convierte el número arábigo Ara en un número romano.

    ####################

    Ara: int
    Número en arábigo

    ####################

    Ara2Rom(44)
    >>> "XLIV"
    """

    Rom=[]
    Arab={}
    Ara=int(Ara)

    for i,j in Roman.items():

        j=int(j)
        Arab[j]=i #El diccionario Roman pero con los key intercambiado por los value
        while Ara//j!=0: #Agrega al resultado el número en Roman más cercano al ingresado, aproximado por abajo
            Ara-=j
            Rom.append(i)

    try:
        n=3
        for i,i1,i2,i3 in zip(Rom[3:],Rom[2:len(Rom)],Rom[1:len(Rom)-1],Rom[:len(Rom)-2]): #Cambia los números que se repiten cuatro veces: IIII XXXX CCCC MMMM
            if i==i1 and i1==i2 and i2==i3:
                Rom.insert(n+1,Arab[int(Roman[i])*5])
                del Rom[n-2:n+1]
                n-=2
            n+=1
    finally:
        try:
            n=2
            for i,i1,i2 in zip(Rom[2:],Rom[1:len(Rom)],Rom[:len(Rom)-1]): #Reemplaza los números de la forma: VIV LXL DCD, a la forma: IX XC CM
                if i==i2 and int(Roman[i1])==int(Roman[i])/5:
                    Rom.insert(n,Arab[int(Roman[i])*2])
                    del Rom[n+1:n+2]
                    del Rom[n-2:n-1]
                    n-=1
                n+=1
        finally:
            return "".join(Rom)

In2=input(Txt.format(Txt3,""))

try:
    Out2=Rom2Ara(In2)
    print(Out2)
except:
    print(Txt1.format(Txt3))