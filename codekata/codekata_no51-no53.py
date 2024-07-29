# no.51 푸드파이트 대회

def solution(food):
    left_side = []

    # 음식의 개수로 좌측 부분 생성
    for i in range(1, len(food)):
        count = food[i] // 2
        left_side.extend([str(i)] * count)

    # 좌측과 우측 대칭 문자열 생성
    result = ''.join(left_side) + '0' + ''.join(left_side[::-1])

    return result

solution([1, 3, 4, 6])