import sys

input = sys.stdin.readline

# Fn = Fn-1 + Fn-2 (n >= 2)


def fib(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n not in memo:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
            return memo[n]
        else:
            return memo[n]


num = int(input())
dictionary = dict()
print(fib(num, dictionary))