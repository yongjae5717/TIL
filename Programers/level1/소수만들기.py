from itertools import combinations


def solution(nums):
    answer = 0
    for i in combinations (nums, 3):
        s = sum (i)
        if is_prime (s):
            answer += 1
    return answer


def is_prime(n):
    num = set (range (2, n + 1))
    for i in range (2, n + 1):
        if i in num:
            num -= set (range (2 * i, n + 1, i))
    if n in num:
        return True
    return False