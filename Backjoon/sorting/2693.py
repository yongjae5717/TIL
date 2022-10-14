import sys

N = int(sys.stdin.readline())
array = list()
result = list()
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
    array[i].sort(reverse=True)
    result.append(array[i][2])

for j in result:
    print(j)