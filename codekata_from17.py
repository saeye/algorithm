# 17. 자연수 뒤집어 배열로 만들기 (자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴)
def solution(n):
    return list(map(int,reversed(str(n))))

print(solution(123))
print(solution(54321))

#