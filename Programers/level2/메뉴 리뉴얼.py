from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = list()
        for o in orders:
            o = list(sorted(o))
            combination = combinations(o, c)
            temp += combination
        counter = Counter(temp)
        max_value = max(counter.values())
        if counter == 0 or max_value == 1:
            break
        for c in zip(counter, counter.values()):
            temp, count = c
            if count == max_value:
                answer.append("".join(temp))
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
