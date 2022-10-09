import sys
sys.setrecursionlimit(100000)

memo = {1: 1, 2: 2}
const = 1234567

def solution(n):
    global memo, const
    if n not in memo:
        memo[n] = solution(n-1) + solution(n-2)
    return memo[n] % const