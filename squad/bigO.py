def my_func(arr, targer):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == targer:
            return mid
        elif arr[mid] < targer:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5]
print(my_func(arr, 4))