a=2
b=10
for i in range(a,b+1):
    f=True
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        print(i)
