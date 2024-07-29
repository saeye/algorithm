array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
output

1 2 3 
4 5 6 
7 8 9 
"""
#
# for row in range(len(array)):
#     for col in range(len(array[row])):
#         print(array[row][col], end=" ")
#         if col == len(array[row])-1:
#             print()


# 출력 코드
# for i in range(len(array)):
#     for j in range(len(array[i])):
#         print(array[i][j], end=" ")
#     # print()


for i in range(len(array)):
    print(' '.join(map(str, array[i])))


