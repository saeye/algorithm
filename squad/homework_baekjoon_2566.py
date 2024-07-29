
matrix = []
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.extend(row)
    print(matrix)

matrix_list = []
for i in range(9):
    row = matrix[i*9:(i+1)*9]
    matrix_list.append(row)

print('\n')
for row in matrix_list:
    print(row)

for j in range(9):
    max(j)