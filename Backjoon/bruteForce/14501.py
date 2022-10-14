import sys

N = int(sys.stdin.readline())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# print(array)
possible = list()
for i in range(N):
    if array[i][0] + i - 1 < N:
        possible.append(array[i][1])
    else:
        possible.append(0)
for j in range(N):
    if possible[j] == 0:
        continue
    for k in range(j):
        if array[k][0] + k - 1 < j:
            possible[j] = max(possible[k] + array[j][1], possible[j])

print(max(possible))