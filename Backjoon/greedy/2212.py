import sys, heapq

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))
array.sort()
distance = list()
for i in range(1, N):
    distance.append(array[i] - array[i-1])
distance.sort(reverse=True)
# print(distance)
if K >= N:
    print(0)
else:
    for _ in range(K-1):
        distance.pop(0)
    print(sum(distance))