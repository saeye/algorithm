# no.51 푸드파이트 대회

def solution(food):
    food_list = []
    for i in food[1:]:
        food_list.extend([i]*int(i))
        food_list.sort()
        if i // 2 == 1:
            int(i) - 1
            print(food_list)

print(solution([1, 7, 2]))
