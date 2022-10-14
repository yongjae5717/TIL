import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
result = list([0])

up_sum = 0
if N == 1:
    print(0)
else:
    for i in range(1, N):
        temp = lst[i] - lst[i-1]
        if temp > 0:
            up_sum += temp
            result.append(up_sum)
        else:
            up_sum = 0
    print(max(result))