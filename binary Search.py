def binarySearch(array, num):
    if num not in array:
        return -1
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == num:
            return mid
        elif array[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(binarySearch([1, 2, 3, 4, 5], 5))  # Output should be 4
