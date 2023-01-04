import sys
input = sys.stdin.readline


def fib(n, memo):
    if n < 2:
        return memo[n]

    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]


def main():
    dictionary = dict()
    dictionary[0] = 0
    dictionary[1] = 1
    n = int(input())
    answer = fib(n, dictionary)
    print(answer)


main()