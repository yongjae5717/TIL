import sys
sys.setrecursionlimit(100000)

memo = {0: 0, 1: 1}
const = 1234567


def solution(n):
    global memo, const
    if n <= 1:
        return memo[n]
    else:
        if n not in memo:
            memo[n] = solution(n-1) + solution(n-2)
        return memo[n] % const