import sys, heapq

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
q = list()

for i in range(N):
    heapq.heappush(q, array[i])

for _ in range(M):
    X = heapq.heappop(q)
    Y = heapq.heappop(q)
    Z = X + Y
    heapq.heappush(q, Z)
    heapq.heappush(q, Z)
print(sum(q))