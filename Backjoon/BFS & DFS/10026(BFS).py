import sys
from collections import deque


def BFS(array_x, s, e, val):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((s, e))

    while q:
        x, y = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < N and 0 <= dy < N and array_x[dx][dy] == val:
                array_x[dx][dy] = 0
                q.append((dx, dy))


N = int(sys.stdin.readline())
array = list(sys.stdin.readline() for _ in range(N))
array_1 = list([0] * N for _ in range(N))
array_2 = list([0] * N for _ in range(N))

for i in range(N):
    for j in range(len(array[i])):
        if array[i][j] == "R":
            array_1[i][j] = 1
            array_2[i][j] = 1
        elif array[i][j] == "G":
            array_1[i][j] = 2
            array_2[i][j] = 1
        elif array[i][j] == "B":
            array_1[i][j] = 3
            array_2[i][j] = 2


cnt_1, cnt_2 = 0, 0
for i in range(N):
    for j in range(N):
        if array_1[i][j] != 0:
            cnt_1 += 1
            BFS(array_1, i, j, array_1[i][j])
        if array_2[i][j] != 0:
            cnt_2 += 1
            BFS(array_2, i, j, array_2[i][j])

print(cnt_1, cnt_2)