def solution(numbers):
    result = set()

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                result.add(numbers[i] + numbers[j])

    result_list = sorted(result)
    return result_list

print(solution([5,0,2,7]))
print(solution([2,1,3,4,1]))