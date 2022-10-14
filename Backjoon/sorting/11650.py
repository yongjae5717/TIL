import sys

N = int(sys.stdin.readline())

array = list()
for i in range(N):
    point = tuple(map(int, sys.stdin.readline().split()))
    array.append(point)

array.sort(key=lambda x: (x[0], x[1]))

for j in array:
    print(j[0], j[1])