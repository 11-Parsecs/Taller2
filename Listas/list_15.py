from random import randint

Txt="Ingrese un mensaje: "

Alpha={}
Pos_Alpha={}
p=0

for i in "abcdefghijklmnopqrstuvwxyz":
    Alpha[p]=i
    Pos_Alpha[i]=p
    p+=1

def Encrypt(N):

    """
    Encripta el string N con el método one-time-pad, devolviendo una tupla
    con el nuevo string y la clave aleatoria utilizada en forma de lista.

    ####################

    N: str
    Texto para encriptar

    ####################

    Encrypt("¡hola mundo!")
    >>> ("¡dxfe nqyrp!",[21,9,19,4,1,21,11,14,26])
    """

    N=list(N.lower())
    N_Enc=[]
    Clave=[]

    for i in N:
        try:
            a=randint(1,26)
            Clave.append(a)
            m=(Pos_Alpha[i]+a)%25
            N_Enc.append(Alpha[m])
        except:
            Clave.pop()
            N_Enc.append(i)

    N_Enc="".join(N_Enc)

    print(N_Enc,Clave)

    return((N_Enc,Clave))

def Decrypt(N_Enc,Clave):

    """
    Desencripta el string N_Enc con el método one-time-pad usando la
    clave Clave, devolviendo el resultado como un string.

    ####################

    N_Enc: str
    Texto para desencriptar

    Clave: list
    Clave para la desencriptación

    ####################

    Encrypt("¡dxfe nqyrp!",[21,9,19,4,1,21,11,14,26])
    >>> "¡hola mundo!"
    """

    N_Enc=list(N_Enc.lower())
    N=[]
    q=0

    for i in N_Enc:
        try:
            m=(Pos_Alpha[i]-Clave[q])%25
            N.append(Alpha[m])
            q+=1
        except:
            N.append(i)

    N="".join(N)

    print(N)

    return(N)

N=input(Txt)
a=Encrypt(N)

N_Enc=input(Txt)
b=Decrypt(N_Enc,a[1])