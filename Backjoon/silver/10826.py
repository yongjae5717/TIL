import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())
dictionary = {0: 0, 1: 1}


def solution(n, memo):
    if n not in memo:
        temp = solution(n - 1, memo) + solution(n - 2, memo)
        memo[n] = temp
    return memo[n]


print(solution(n, dictionary))