import sys
import heapq

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
low = 0
for _ in range(N-1):
    A = list(map(int, sys.stdin.readline().split()))
    while len(A) != 0:
        temp = heapq.heappop(A)
        heapq.heappush(array, temp)
        heapq.heappop(array)

print(array[0])