import sys
import heapq

N = int(sys.stdin.readline())
q = list()
for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, temp)