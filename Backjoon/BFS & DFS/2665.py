"""
N x N의 바둑판
흰방(1): 통과가 가능하다
검은방(0): 통과가 불가능하다
(1,1)에서 (8,8)을 가기 위해서 검은방을 흰방으로 최소한으로 바꿔서 통과하라
"""

import sys
from collections import deque


def BFS(board):
    q = deque()
    q.append((0, 0))
    visited = list([-1] * N for _ in range(N))
    # 처음 위치는 방문한 것으로 가정
    visited[0][0] = 0

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        # print(q)
        x, y = q.popleft()
        # 도착지에 도착했을 경우 return
        if x == N-1 and y == N-1:
            return visited[x][y]
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if (0 <= dx < N) and (0 <= dy < N) and visited[dx][dy] == -1:
                # 흰방일 경우
                if board[dx][dy] == 1:
                    # 우선탐색
                    q.appendleft((dx, dy))
                    visited[dx][dy] = visited[x][y]
                # 검은방일 경우
                else:
                    q.append((dx, dy))
                    visited[dx][dy] = visited[x][y] + 1


N = int(sys.stdin.readline())
board = list()
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().strip())))

print(BFS(board))