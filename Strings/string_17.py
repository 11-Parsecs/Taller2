Str="abcdefghijklomnopqrstuvwxyz"

for p in Str:
    print(Str)
    ABC=list(Str)
    n=ABC[0]
    BCD=ABC[1:]
    BCD.append(n)
    Str="".join(BCD)