from itertools import product


def solution(word):
    lst = list("AEIOU")
    result = list()
    for i in range(1, 6):
        for p in product(lst, repeat=i):
            temp = "".join(p)
            result.append(temp)
    result.sort()
    return result.index(word) + 1


print(solution("AAAAE"))

print(solution("AAAE"))

print(solution("I"))

print(solution("EIO"))