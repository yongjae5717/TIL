from collections import Counter


def solution(topping):
    answer = 0
    counter = Counter(topping)
    check = set()
    for i in topping:
        counter[i] -= 1
        check.add(i)
        if counter[i] == 0:
            counter.pop(i)
        if len(counter) == len(check):
            answer += 1
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))
