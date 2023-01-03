import sys
input = sys.stdin.readline


def main():
    n = int(input())
    chain = list(map(int, input().split()))

    chain.sort()

    result = 0
    for i in range(n):
        count = n - i - 1
        result += chain[i]
        if result >= count:
            print(count)
            break


main()