import sys
input = sys.stdin.readline


def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer


x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(solution(x, y))