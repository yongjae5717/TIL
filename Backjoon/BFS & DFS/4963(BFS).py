import sys
from collections import deque


def BFS(s, e):
    d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    q.append((s, e))
    while q:
        y, x = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if (0 <= dx < W) and (0 <= dy < H) and (array[dy][dx] == 1):
                array[dy][dx] = 0
                q.append((dy, dx))


end = "0 0"
insert = ""
result = list()
while insert != end:
    W, H = map(int, sys.stdin.readline().split())
    insert = str(W) + " " + str(H)
    array = list()
    for i in range(H):
        temp = list(map(int, sys.stdin.readline().split()))
        array.append(temp)

    count = 0
    q = deque()
    for i in range(H):
        for j in range(W):
            if array[i][j] != 0:
                count += 1
                BFS(i, j)
    result.append(count)


for i in range(len(result) - 1):
    print(result[i])