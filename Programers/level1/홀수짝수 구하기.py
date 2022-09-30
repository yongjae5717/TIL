import sys


def solution(num):
    if num % 2 == 1:
        return "Odd"
    return "Even"


n = int(sys.stdin.readline())
print(solution(n))