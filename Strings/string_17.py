##########################
#Escriba un programa que genere 26 strings con el abecedario, pero en cada uno que empiece por la siguiente letra del mismo
##########################

Str="abcdefghijklomnopqrstuvwxyz"

for p in Str:
    print(Str)
    ABC=list(Str)
    n=ABC[0]
    BCD=ABC[1:]
    BCD.append(n)
    Str="".join(BCD)