import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
ascii_code = list([] for _ in range(n))
lst = [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25]
verb = [0, 2, 8, 13, 19]


for i in range(n):
    word = input().strip()[4:-4]
    temp = list(verb)
    for c in word:
        if ord(c)-ord("a") not in temp:
            temp.append(ord(c)-ord("a"))
            ascii_code[i].append(ord(c)-ord("a"))


def solution(k, ascii_code):
    answer = 26
    if k < 5:
        return 0

    for combination in combinations(lst, k - 5):
        temp = list(combination) + list(verb)
        result = 26
        for a in ascii_code:
            if is_contain(a, temp):
                result -= 1
        answer = min(answer, result)
    return 26 - answer


def is_contain(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True


print(solution(k, ascii_code))