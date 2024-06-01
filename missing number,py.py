array=[1,2,3,4,6]
for i in range(min(array),max(array)):
    if i not in array:
        print(i)
        break