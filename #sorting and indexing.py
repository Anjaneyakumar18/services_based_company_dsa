#sorting and indexing
array=[1,2,3,4,5,6,6]
array=list(set(array))
array.sort()
print(array[-2])
#finding large and eliminating
array1=[1,2,3,4,5,6]
array1.remove(max(array1))
print(max(array1))