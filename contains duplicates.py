array=[1,2,3,4,4,5,6]
dub_set=set()
for num in array:
    if num in dub_set:
        print(f'duplicate number is {num}')
        break
    else:
        dub_set.add(num)
        