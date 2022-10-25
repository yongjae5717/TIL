from itertools import permutations


def solution(numbers):
    lst = list(numbers)
    result = list()
    permutation = list()
    for i in range(1, len(numbers) + 1):
        permutation += list(permutations(lst, i))

    strToIntNumber = set(int("".join(p)) for p in permutation)

    for n in strToIntNumber:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
                break
        if check:
            result.append(1)

    return sum(result)


print(solution("17"))
print(solution("011"))