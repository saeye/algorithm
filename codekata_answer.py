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


