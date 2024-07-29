"""
문제 이해

행렬 두개 더하는 거임

1. 일단 행렬 입력 받아서 저장해야함
2. 각 인덱스 계산해서 자리수마다 더해야함
3. 결과 행렬 포맷 맞춰서 출력 해야함

"""

n, m = map(int, input().split())
matrix_a = []
for i in range(n):
    row = []
    row_input = input()
    row_input_list = row_input.split()
    row_input_int_list = list(map(int, row_input_list))
    matrix_a.append(row_input_int_list)


matrix_b = []
for i in range(n):
    row = []
    row_input = input()
    row_input_list = row_input.split()
    row_input_int_list = list(map(int, row_input_list))
    matrix_b.append(row_input_int_list)


"""
1. 결과 매트릭스를 만들어두고
2. 각각 인덱스를 이용해서 더한다음, 결과 매트릭스에 저장
3. 결과 매트릭스 출력
"""


def add_matrix(matrix_a, matrix_b):
    """
    a[i][j] + b[i][j]
    """
    result_matrix = []

    for i in range(n):
        result_row = []
        for j in range(m):
            each_sum = matrix_a[i][j] + matrix_b[i][j]
            result_row.append(each_sum)
        result_matrix.append(result_row)

    return result_matrix


rlt = add_matrix(matrix_a, matrix_b)


for i in range(n):
    str_row = list(map(str, rlt[i]))
    print_row = " ".join(str_row)
    print(print_row)


