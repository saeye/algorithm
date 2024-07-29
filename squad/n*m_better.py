# 입력을 받기 위한 함수
def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


# 행렬을 더하는 함수
def add_matrices(a, b, n, m):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


# 행렬을 출력하는 함수
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


n, m = map(int, input().split())
matrix_a = read_matrix(n, m)
matrix_b = read_matrix(n, m)
matrix_c = add_matrices(matrix_a, matrix_b, n, m)
print_matrix(matrix_c)
