array=[1,2,3,4,5,6,7,8,9,10]
min,max=array[0],array[0]
for num in array:
    if num>max:
        max=num
    elif num<min:
        min=num
print(f'maximum:{max}\nMinimum:{min}')
