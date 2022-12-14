import sys
from collections import deque
input = sys.stdin.readline


def make_board(m, n, k):
    board = list(list([0] * n) for _ in range(m))
    for _ in range(k):
        x_1, y_1, x_2, y_2 = map(int, input().split())
        for x in range(x_1, x_2):
            for y in range(y_1, y_2):
                board[y][x] = 1
    return board


def bfs(m, n, board):
    q = deque()
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    area = list()

    for i in range(m):
        for j in range(n):
            if not board[i][j]:
                board[i][j] = 1
                q.append((i, j))
                area.append(1)
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < m and 0 <= ny < n and not board[nx][ny]:
                            q.append((nx, ny))
                            board[nx][ny] = 1
                            area[-1] += 1
    return sorted(area)


def solution():
    m, n, k = map(int, input().split())
    board = make_board(m, n, k)
    area = bfs(m, n, board)

    print(len(area))
    print(*area)


solution()