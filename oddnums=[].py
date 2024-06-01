oddnums=[]
evennums=[]
array_nums=[1,2,3,4,5,6,7,8]
for i in range(len(array_nums)):
    if array_nums[i]%2==0:
        evennums.append(array_nums[i])
    else:
        oddnums.append(array_nums[i])
print(f'even numbers:{evennums}\nodd numers:{oddnums}')