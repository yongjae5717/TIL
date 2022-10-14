import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
q.append((0, 0))


def BFS():
    while q:
        x, y = q.popleft()
        print(x, y)
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < N and 0 <= dy < M and maze[dx][dy] == 1:
                maze[dx][dy] = maze[x][y] + 1
                q.append((dx, dy))
                # for j in maze:
                #     print(j)
                # print("\n")


maze[0][0] = 1
BFS()
print(maze[N-1][M-1])