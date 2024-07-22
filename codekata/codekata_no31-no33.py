# 31. 수박수박수박수박수박수?
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 생각
# 무한히 반복되는 수박 문자열 생성
# n만큼 return

import itertools

# 무한히 반복되는 수박 문자열 생성
loop_word = itertools.cycle('수박')
def solution(n):
    # for _ in 반복 횟수만 사용, 무한반복 수박문자열을 n개 return
    return ''.join(next(loop_word) for _ in range(n))

print(next(loop_word))
print(next(loop_word))
print(solution(2))
print(solution(3))
print(solution(4))

# 32. 내적
# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
# 입출력 예
# a [-1,0,1] b [1,0,-1] 일 때, a와 b의 내적은 (-1)*1 + 0*0 + 1*(-1) = -2

def solution(a, b):
    return sum(a[i] * b[i] for i in range(len(a))) # a와 b의 같은 인덱스에 있는 요소를 길이만큼 반복해서 곱해주고 sum

print(solution([-1,0,1], [1,0,-1]))
print(solution([2,-1,], [-1,-2]))


# 33. 약수의 개수와 덧셈
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서,
# 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return

def solution(left, right):
    left_divisor = []
    right_divisor = []
    left_divisor = [i for i in range(left+1) if i % 2 == 0]
    right_divisor = [i for i in range(right+1) if i % 2 == 1]
    len(left_divisor)
    len(right_divisor)
    return sum(int(i) if i % 2 == 0 else -int(i) for i in range(left, right+1))
