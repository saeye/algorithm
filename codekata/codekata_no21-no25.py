# 21.하샤드 수
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

def is_harshad(x):
    sum_digit = sum(int(digit) for digit in str(x))
    return x % sum_digit == 0

print(is_harshad(1729))
print(is_harshad(123))


# 22. 두 정수 사이의 합
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수(예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴)
def solution(a, b):
    if a < b:
        return sum(int(i) for i in range(a, b+1))
    if a > b:
        return sum(int(i) for i in range(b, a+1))
    else:
        return a

print(solution(3, 5))
print(solution(4, 2))


# 23. 콜라츠 추측 (주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측)
 # 1-1. 입력된 수가 짝수라면 2로 나눕니다.
 # 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
 # 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다.
# 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요.
# 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

def solution(num):
    if num == 1:
        return 0

    count = 0
    while num != 1: # num이 1이 아니면 계속 반복문 돌리기
        if num % 2 == 0:
            num = num // 2
        elif num % 2 != 0:
            num = num*3 + 1

        count += 1

        if count == 500:
            return -1

    return count

print(solution(6))


# 24. 서울에서 김서방 찾기
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
# 입출력 예
# seoul = ["Jane", "Kim"]
# "김서방은 1에 있다"

def solution(seoul):
    x = seoul.index("Kim")
    return f"김서방은 {x}에 있다"

seoul = ["Kim", "Lee", "Jane"]
print(solution(seoul))


# 25.나누어 떨어지는 숫자 배열
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
def solution(arr, divisor):

    valid_arrays = [i for i in arr if i % divisor == 0] # arr를 돌면서 divisor로 나누었을 때 떨어지는 요소 i 리스트 생성

    if not valid_arrays: # 만약 나누어 떨어지는 요소가 없으면
        return [-1]        # 배열에 -1을 담아 반환

    valid_arrays.sort()  # 오름차순 정렬 ( sort()메소드는 정렬을 할 뿐 None을 반환한다)

    return valid_arrays

print(solution([5,9,7,10], 5))
print(solution([5,9,7], 10))

