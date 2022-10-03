def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            val = numbers[i] + numbers[j]
            if val not in answer:
                answer.append(val)
    answer.sort()
    return answer


def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            val = numbers[i] + numbers[j]
            answer.append(val)
    return sorted(list(set(answer)))