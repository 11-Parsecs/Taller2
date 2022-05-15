Txt="Ingrese una secuencia propia de 8 términos: "
Txt1="Las listas que coinciden con su secuencia son:"

L=['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

Sec=input(Txt)

Coinc={}

for i,j in enumerate(Sec):
    if j != "*":
        Coinc[i]=j

L_Rem=list(L)

for Str in L:
    for i,j in Coinc.items():
        if Str[i]!=j:
            try:
                L_Rem.remove(Str) 
            except:
                L_Rem=L_Rem

print(Txt1)
print(L_Rem)