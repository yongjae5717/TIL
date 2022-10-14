import sys, heapq

N = int(sys.stdin.readline())
q = list()
for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if q:
            x, y = heapq.heappop(q)
            print(x * y)
        else:
            print(0)
    else:
        if temp >= 0:
            heapq.heappush(q, (abs(temp), 1))
        else:
            heapq.heappush(q, (abs(temp), -1))