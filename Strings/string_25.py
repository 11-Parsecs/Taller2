# 3x+4y -> 3*x+4*y
# 3(x+5) -> 3*(x+5)

Txt1="Ingrese una expresión algebraica: "

A=input(Txt1)
B=list(A)
N=[]

p=0
n_i=A[0]

for n in B:
    
    if n_i.isdigit() and not n.isdigit() and not n in ")/^+-":
        B.insert(p,"*")
    
    n_i=n
    p+=1

C="".join(B)
print(C)
C.replace("^","**")
print(eval(C))