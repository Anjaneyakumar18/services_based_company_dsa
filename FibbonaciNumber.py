#list Data Type Useage
Fib=[0,1]
for i in range(8):
    Fib.append(Fib[-1]+Fib[-2])
print(Fib)
#using Iteration
num1=0
num2=1
for i in range(10):
    temp=num1
    num1=num2
    num2=temp+num1
    print(temp)