from itertools import permutations


def solution(number):
    lst = [sum(permutation) for permutation in permutations(number, 3)]
    return lst.count(0)//6


print(solution([-2, 3, 0, 2, -5]))

print(solution([-3, -2, -1, 0, 1, 2, 3]))

print(solution([-1, 1, -1, 1]))