# 예제 배열
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


"""
output

1 2 3 4
5 8
9 12
13 14 15 16

"""

# 일단 리스트에서 빼고
# row[1][1:3] row[2][1:3] 을 없애나..

# for row in range(len(array)):
#     # print(array[row])
#     print(' '.join(map(str, array[row])))

def array_edge(row):
    # 6, 7 삭제
    if row == 1:
        print(array[row][0],array[row][3])
    # 10, 11 삭제
    elif row == 2:
        print(array[row][0],array[row][3])
    # 나머지가 row들은 정상적으로 출력
    else:
        print(' '.join(map(str, array[row])))


for i in range(len(array)):
    array_edge(i)



