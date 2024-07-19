# 26. 음양 더하기
# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
#제한사항
#absolutes의 길이는 1 이상 1,000 이하입니다.
#absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
#signs의 길이는 absolutes의 길이와 같습니다.
#signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

def solution(absolutes, signs):
    # signs의 각 인덱스 값으로 요소를 판단해야하므로
    for i in range(len(signs)):
        if signs[i]:  # signs[i]가 True면
            absolutes[i] = int(absolutes[i])
        else:         # if문의 조건이 False인 경우, 즉 signs[i]가 False
            absolutes[i] = -int(absolutes[i])

    return sum(absolutes)

print(solution([1,2,2],	[True,False,True]))
print(solution([1,1,2],	[True,True,False]))


# 27. 핸드폰 번호 가리기
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# phone_number는 길이 4 이상, 20이하인 문자열입니다.

#입출력 예
# phone_number "01033334444" return	"*******4444"

def solution(phone_number):
        # phone_number의 길이를 구하고 4를 빼준 만큼 "*"를 곱해서 *로 표기하고
        # phone_number의 마지막에서 네자리를 붙여준다. (index-1은 맨 마지막 값)
        return "*" * (len(phone_number) - 4) + phone_number[-4:]

print(solution("01033334444"))


# 28. 없는 숫자 더하기
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.

# 입출력 예
# numbers [5,8,4,0,6,7,9]  result 6

def solution(numbers):
    basic_numbers = list(range(0, 10))
    return sum(i for i in basic_numbers if i not in numbers)

print(solution([5,8,4,0,6,7,9]))
print(solution([3,4,5,8,0,6,7,9]))


# 29. 가장 작은 수 제어하기
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
# 입출력 예
# arr [4,3,2,1]	return [4,3,2]
# arr [10]	return [-1]

def solution(numbers):
    if len(numbers) == 1:
        return [-1]

    min_number = min(numbers)

    return list(i for i in numbers if i != min_number)

print(solution([4,3,2,1]))
print(solution([10]))


# 30. 가운데 글자 가져오기
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# [풀이]
# 문자열의 길이 구하기
# 짝 홀 판단
# 가운데 문자 return

def solution(s):
    s_word = list(s)
    if len(s_word) % 2 == 1:
        return s_word[(len(s_word) // 2)]
    else:
        return ''.join(s_word[(len(s_word) // 2) - 1 : (len(s_word) // 2) + 1])

print(solution("abcde"))
print(solution("abcd"))
print(solution("12345"))
print(solution("123456"))