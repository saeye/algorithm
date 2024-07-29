# 예제 배열
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 제곱한 배열 생성
squared_array = []

squared_array = [[x **2 for x in row ] for row in array]
print(squared_array)

for i in squared_array:
    print(i)

"""
output

[1, 4, 9]
[16, 25, 36]
[49, 64, 81]

"""