import sys, heapq
input = sys.stdin.readline

n = int(input())
lst = list()

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(lst, -x)
    else:
        if len(lst) != 0:
            print(-heapq.heappop(lst))
        else:
            print(0)