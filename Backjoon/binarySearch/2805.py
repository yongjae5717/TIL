import sys


# 나무의 수 N, 나무의 길이 M
N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(A)
result = 0

while start <= end:
    mid = (start + end) // 2

    # ???변경전
    #     for i in A:
    #         if i - mid > 0:
    #             sum += i - mid

    # ??? 시간초과 (변경후)
    s = sum(i - mid if i > mid else 0 for i in A)

    if s < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)