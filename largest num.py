#logical operation
num1=10
num2=20
num3=30
if (num1>num2) and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
# using max()
print(max(num1,num2,num3))