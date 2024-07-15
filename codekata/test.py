def solution(n):
    n_list = list((map(int, str(n))))
    reversed_list = sorted(n_list, reverse=True)
    reversed_list_to_int = int(''.join(map(str, reversed_list))) # join은 문자열로 구성된 것만 결합
    return reversed_list_to_int

print(*map(int, str(132)))
print(solution(132))

x = 1234
for digit in str(x):
    print(digit)

list = [1]

if list:
    print("Qyd")