##########################
#Suponga que tiene la siguiente lista de strings:
#L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
#El usuario ingresa un string con solo algunas letras y el resto son asteriscos. Por ejemplo a**a****.
#El usuario desea saber cuáles de los strings de la lista coincide con su patrón. En el ejemplo dado serían el primero y el cuarto.
#Escruba un programa que realuce esto.
##########################

Txt="Ingrese una secuencia propia de 8 términos: "
Txt1="Las listas que coinciden con su secuencia son:"

L=['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

Sec=input(Txt)

Coinc={}

for i,j in enumerate(Sec): #Guarda las posiciones de las letras que no son asteriscos en el string ingresado
    if j != "*":
        Coinc[i]=j

L_Rem=list(L) #Copia la lista de strings para poder remover objetos sin problemas

for Str in L:
    for i,j in Coinc.items():
        if Str[i]!=j: #Verifica la coincidencia de strings con las posiciones
            try:
                L_Rem.remove(Str) #Elimina de la copia los strings que no coincidan
            except:
                L_Rem=L_Rem

print(Txt1)
print(L_Rem)