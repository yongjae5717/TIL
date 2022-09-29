import sys
input = sys.stdin.readline

"""
0의 개수: fib(n-1)의 값과 동일
1의 개수: fib(n)과 동일
"""


def fib(num, memo):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        if num not in memo:
            memo[num] = fib(num-1, memo) + fib(num-2, memo)
            return memo[num]
        else:
            return memo[num]


t = int(input())
for _ in range(t):
    n = int(input())
    dictionary = dict()
    if n == 0:
        print(1, fib(n, dictionary))
    else:
        print(fib(n-1, dictionary), fib(n, dictionary))

