num=11
f=True
for i in range(2,num):
    if num%i==0:
        f=False
        print("Not Prime")
        break
if f:
    print("Prime number")