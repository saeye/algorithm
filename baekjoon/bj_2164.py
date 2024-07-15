# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복. 우선, 제일 위에 있는 카드를 바닥에 버리고 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 예를 들어 N=4인 경우. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다.
# 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

from collections import deque

def last_card_deq(num):
    card_numbers = list(i for i in range(1, num + 1))
    deq = deque(card_numbers)

    while len(deq) > 1:  # 카드 한장 남을 때까지 반복
        deq.popleft()    # 맨 위(맨 왼쪽) 카드 제거
        deq.append(deq.popleft())  # 맨 위(맨 왼쪽) 카드를 맨 오른쪽으로 이동
    return deq.popleft() # 마지막 남은 카드 반환

print(last_card_deq(4))
print(last_card_deq(5))
print(last_card_deq(6))
print(last_card_deq(7))


# card_numbers list를 따로 만들지 않고 바로 deq의 객체로 넣어서 수정한 코드

def last_card_deq(num):
    deq = deque(range(1, num + 1)) # 1부터 n까지의 카드를 데크에 바로 넣어어서 리스트화 한다.

    while len(deq) > 1:  # 카드 한장 남을 때까지 반복
        deq.popleft()    # 맨 위(맨 왼쪽) 카드 제거
        deq.append(deq.popleft())  # 맨 위(맨 왼쪽) 카드를 맨 오른쪽으로 이동
    return deq.popleft() # 마지막 남은 카드 반환

print(last_card_deq(4))
print(last_card_deq(5))
print(last_card_deq(6))
print(last_card_deq(7))