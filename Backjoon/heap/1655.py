import sys, heapq

# 1~2: 1, 3~4: 2, 5~6: 3 ......
N = int(sys.stdin.readline())
q = list()
t = list()
for i in range(N):
    temp = int(sys.stdin.readline())
    if i % 2 == 1:
        heapq.heappush(q, temp)
    else:
        heapq.heappush(t, -temp)

    if q and -t[0] > q[0]:
        heapq.heappush(q, -heapq.heappop(t))
        heapq.heappush(t, -heapq.heappop(q))

    print(t[0])