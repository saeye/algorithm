# 두수의 곱
def solution(num1, num2):
    return num1*num2

# 두수의 몫
def solution(num1, num2):
    answer = num1 // num2
    return answer

# 나이 구하기
def solution(age):
    answer = 2022 - age + 1
    return answer

# 숫자 비교하기
def compare_numbers(num1, num2):
    return 1 if num1 == num2 else -1

# 두 수의 합 / 근데 프로그래머스에서는 함수명을 solution으로 해야만 정답처리를 한다.
def plus_numbers(num1, num2):
    return num1 + num2

# 두 수의 나눗셈
def solution(num1, num2):
    return int((num1 / num2)*1000)


# 각도기
def solution(angle):
    angle = int(angle)
    if 0 < angle < 90 :
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
    else:
        return "angle은 0보다 크고 180 이하의 각입니다."


# 짝수의 합(정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성하시오)
def solution(n):
    n = int(n)
    even_sum = 0
    for i in range(1, n+1): # range함수는 마지막 값 포함X
        if i % 2 == 0:
            even_sum += i
        else:
            even_sum
    return even_sum


# 배열의 평균값
def solution(numbers):
    average_num = sum(numbers)/len(numbers)
    return average_num


# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성하시오
def solution(num):
    num = int(num)
    if num % 2 == 0 :
        return "Even"
    else:
        return "Odd"


# 평균 구하기 (정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성하시오)
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer


# 자릿수 더하기
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
def solution(n):
    n_str = str(n)
    sum_digit = 0
    for digit in n_str :
        digit_int = int(digit)
        sum_digit += digit_int
    return sum_digit


# map 사용하니까 더 간단하게 구할 수 있다.
def solution(n):
    n_str = str(n)
    return sum(map(int, n_str))


# 약수의 합 (정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성하기)
def solution(n):
    sum_divisors = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors


# 나머지가 1이 되는 수 찾기
# (자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수 완성하기)
def solution(n):
    for x in range(1,n+1):
        if n % x == 1:
            return x


# x만큼 간격이 있는 n개의 숫자 (정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴)
def solution(x, n):
    xn = []
    for i in range(1,n+1):
        xn.append(x*i)
    return xn


