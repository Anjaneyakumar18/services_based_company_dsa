#arthematic
number=1024
sum=0
while number>0:
    sum+=number%10
    number//=10
print(sum)
#string
num=1024
s=str(num)
sums=0
for i in range(len(s)):
    sums+=int(s[i])
print(sums)
