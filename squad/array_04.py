# 예제 배열
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

"""
output

[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

"""

lst = []

lst.extend(array[0][:])
lst.extend(array[1][3:])
lst.extend(array[2][3:])
lst.extend(array[3][::-1])
lst.extend(array[2][0:1])
lst.extend(array[1][:3])
lst.extend(array[2][2:3])
lst.extend(array[2][1:2])


print(lst)
