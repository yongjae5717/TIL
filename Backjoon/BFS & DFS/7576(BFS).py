import sys
from collections import deque


def BFS():
    d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    count = -1
    global M, N, array
    while q:
        count += 1
        for _ in range(len(q)):
            x, y = q.popleft()

            for k in range(len(d)):
                dx = x + d[k][0]
                dy = y + d[k][1]

                if (0 <= dx < N) and (0 <= dy < M) and (array[dx][dy] == 0):
                    array[dx][dy] = array[x][y] + 1
                    q.append((dx, dy))
    for i in array:
        if 0 in i:
            return -1
    return count


M, N = map(int, sys.stdin.readline().split())
array = list()
q = deque()

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if temp[j] == 1:
            q.append((i, j))
    array.append(temp)


print(BFS())