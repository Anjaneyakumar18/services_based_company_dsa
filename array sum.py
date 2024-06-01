#using simple sum()
array=[1,2,3,4,5]
print(sum(array))
#using addition
array_sum=0
for i in range(len(array)):
    array_sum+=array[i]
print(array_sum)
#dynamic list elements 
array_nums=list(map(int,input("Elements with space saparations").split()))
print(sum(array_nums))