number=1024
sum=0
while number>0:
    sum+=number%10
    number//=10
print(sum)