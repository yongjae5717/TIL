import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    number = list(map(int, input().split()))
    return max(number) * min(number)


print(solution())