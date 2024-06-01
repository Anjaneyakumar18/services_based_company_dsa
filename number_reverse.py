#method1 Arthematic opeartors
num=1234
final=0
while num>0:
    temp=num%10
    final=final*10+temp
    num//=10
print(f"Reversed Number is {final}")
#String Method
num=1234
print(f"reversed number is {int(str(num)[::-1])}")