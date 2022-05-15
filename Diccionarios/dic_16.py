Txt="Ingrese un número {}{}: "
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

    Ara=0

    Inv=Rom[::-1]

    n_i1=0

    for i in Inv:
        n_i=eval(Roman[i])
        if n_i1>n_i:
            if n_i in [5,50,500]:
                Ara=Txt4
                break
            elif n_i1/10 != n_i:
                if n_i1==5 and n_i==1:
                    Ara-=1
                else:
                    Ara=Txt4
                    break
            else:
                Ara-=n_i
        else:
            Ara+=n_i
        n_i1=n_i
    return Ara
"""
In1=input(Txt.format(Txt2,Txt5))

try:
    Out1=Rom2Ara(In1)
    print(Out1)
except:
    print(Txt1.format(Txt2))
"""

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
    Ara=int(Ara)

    for i,j in Roman.items():

        j=int(j)
        while Ara//j!=0:
            Ara-=j
            Rom.append(i)

    return "".join(Rom)

In2=input(Txt.format(Txt3,""))

Out2=Ara2Rom(In2)
print(Out2)

'''
try:
    Out2=Rom2Ara(In2)
    print(Out2)
except:
    print(Txt1.format(Txt3))
'''