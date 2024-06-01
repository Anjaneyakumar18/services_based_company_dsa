#Method1 with out using third variable
a=10 
b=20
a=a+b
b=a-b
a=a-b
print(f'a={a} and b={b}')
#method2 using third variable
c=10
d=20
temp=c
c=d
d=temp
print(f'c ={c},d={d}')
#method3 Packing and Unpacking
e=10
f=20
e,f=f,e
print(f"e={e},f={f}")
#method4 Bitwise Operators
g=10
h=20
g=g^h
h=g^h
g=g^h
print(f'g={g},h={h}')