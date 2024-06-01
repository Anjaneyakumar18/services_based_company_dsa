#method1 Using Arthematic Operators
num=1634
to_check=num
num_dup=num
len=0
while num>0:
    len+=1
    num//=10
sum=0
while num_dup>0:
    temp=num_dup%10
    sum+=temp**len
    num_dup//=10
print(f'Number:{to_check} and after operation {sum} Hence, armstrong  {sum==to_check}')