def solution(price, money, count):

    # 부족한 금액 = 총비용 - 부족한금액
    # 총 비용 계산
    total_cost = price * (count * (count + 1)) // 2
    # 부족한 금액 계산
    shortfall = total_cost - money

    # 부족한 금액이 0보다 작으면 0을 반환
    return max(shortfall, 0)
