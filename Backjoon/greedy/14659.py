import sys

N = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
check = top[0]
result = list()
count = 0
for i in range(1, N):
    if check > top[i] and i != N - 1:
        count += 1
    elif check > top[i] and i == N - 1:
        count += 1
        result.append(count)
    else:
        check = top[i]
        result.append(count)
        count = 0
# print(result)
print(max(result))