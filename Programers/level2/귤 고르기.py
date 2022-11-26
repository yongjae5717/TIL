from collections import Counter


def solution(k, tangerine):
    counter = Counter(tangerine)
    lst = list(counter.values())
    lst.sort(reverse=True)

    answer = 0
    value = 0
    for count in lst:
        if value >= k:
            break
        answer += 1
        value += count
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))