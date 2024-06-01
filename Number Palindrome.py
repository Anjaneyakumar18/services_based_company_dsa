#Arthematic
num=11211
num2=num
final=0
while num>0:
    temp=num%10
    final=final*10+temp
    num//=10
print(f"Number is palindrome:{num2==final}")
#String Operation
numb=11211
print("Given Number Palindrome :",int(str(numb))==int(str(numb)[::-1]))