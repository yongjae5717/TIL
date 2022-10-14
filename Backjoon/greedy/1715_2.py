import sys
import heapq

N = int(input())
C = []

for _ in range(N):
    heapq.heappush(C, int(sys.stdin.readline()))

if len(C) == 1:
    print(0)
else:
    ans = 0
    while len(C) > 1:
        temp1 = heapq.heappop(C)
        temp2 = heapq.heappop(C)
        print(C, temp1, temp2)
        ans += temp1 + temp2
        heapq.heappush(C, temp1 + temp2)
    print(ans)