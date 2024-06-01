def linearSearch(array,num):
    for i in range(len(array)):
        if array[i]==num:
            return f'search element found at {i} index'
array=[1,2,3,4,5,6,7,8,9,0,5]
print(linearSearch(array,0))