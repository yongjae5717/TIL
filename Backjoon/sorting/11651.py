import sys

N = int(sys.stdin.readline())

array = list()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    array.append((x, y))
array.sort(key=lambda c: (c[1], c[0]))

for i in array:
    print(i[0], i[1])