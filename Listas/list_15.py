from random import randint

Txt="Ingrese un mensaje: "
Txt1="No debe contener números."

Alpha={}
Pos_Alpha={}
p=0

for i in "abcdefghijklmnopqrstuvwxyz":
    Alpha[p]=i
    Pos_Alpha[i]=p
    p+=1

def Encrypt():

    while True:
        N=input(Txt)
        if N.isalpha():
            break
        else:
            print(Txt1)

    N=list(N.lower())
    N_Enc=[]
    Clave=[]

    for i in N:
        a=randint(1,26)
        Clave.append(a)
        m=(Pos_Alpha[i]+a)%25
        N_Enc.append(Alpha[m])

    N_Enc="".join(N_Enc)

    print(N_Enc,Clave)

    return((N_Enc,Clave))

def Decrypt(Clave):

    while True:
        N_Enc=input(Txt)
        if N_Enc.isalpha():
            break
        else:
            print(Txt1)
    
    N_Enc=list(N_Enc.lower())
    N=[]
    q=0

    for i in N_Enc:
        m=(Pos_Alpha[i]-Clave[q])%25
        N.append(Alpha[m])
        q+=1

    N="".join(N)

    print(N)

    return(N)

a=Encrypt()
b=Decrypt(a[1])