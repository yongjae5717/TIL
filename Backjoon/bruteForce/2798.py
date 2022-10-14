import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
# print(array)
result = list()
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1 = array[i]
            x2 = array[j]
            x3 = array[k]
            ans = x1 + x2 + x3
            if ans <= M:
                result.append(ans)

print(max(result))