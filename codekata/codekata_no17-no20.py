# 17. 자연수 뒤집어 배열로 만들기 (자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴)
def solution(n):
    return list(map(int,reversed(str(n))))

print(solution(123))
print(solution(54321))


# 18. 문자열을 정수로 바꾸기 (문자열 s를 숫자로 변환한 결과를 반환하는 함수 solution 완성하기)
def solution(s):
    return int(s)

print(solution("-1243"))
print(solution("2234"))
print(solution("-19304"))


# 19. 정수 제곱근 판별 (n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴)
def solution(n):
    x = int(n ** 0.5) # 변수 x를 정의하는 동시에 n의 제곱근의 정수부분을 구함
    if n == x ** 2:
        return (x+1)**2
    else:
        return -1


# 20. 정수 내림차순으로 배치하기 (정수 n을 매개변수로 입력받는다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴)
# 예를들어 n이 118372면 873211을 리턴
def solution(n):
    n_list = list((map(int, str(n))))
    reversed_list = sorted(n_list, reverse=True)
    reversed_list_to_int = int(''.join(map(str, reversed_list))) # join은 문자열로 구성된 것만 결합
    return reversed_list_to_int

print(*map(int, str(132)))
print(solution(132))