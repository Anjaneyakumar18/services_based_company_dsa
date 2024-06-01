#BackTracking
def Fact(num):
    if num==0:
        return 1
    return num*Fact(num-1)
print(f'Factorial is {Fact(5)}')
#Looping
num=5
fact=1
while num>0:
    fact*=num
    num-=1
print(f"Fatorial is {fact}")