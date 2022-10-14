import sys

N = 9
array = list()
for _ in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
s = sum(array)
x, y = 0, 0
for i in range(N):
    for j in range(i + 1, N):
        if s - array[i] - array[j] == 100:
            x, y = i, j
for k in range(N):
    if k == x or k == y:
        continue
    else:
        print(array[k])
