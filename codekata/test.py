def fibo(n):
    if n == 0:
        return f"0번째 수는 없음 None"
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    fibo_num_list = [1, 1]
    for i in range(2, n+1):
        fibo_num_list.append(fibo_num_list[i-2] + fibo_num_list[-1])

    return fibo_num_list[n-1]

n = int(input(f"n번째 피보나치 수는? 숫자 n을 입력하세요"))
print(fibo(n))

# print(fibo(0)) # 0번째?: None
# print(fibo(1)) # 1
# print(fibo(5)) # 5
# print(fibo(6)) # 8
# print(fibo(10)) # 55
