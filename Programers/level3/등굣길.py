from collections import deque


def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1
    for i in puddles:
        x, y = i
        board[y-1][x-1] = -1

    d = [(1, 0), (0, 1)]
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx <= n-1 and 0 <= dy <= m-1:
                if board[dx][dy] >= 0:
                    board[dx][dy] += board[x][y]
                    if (dx, dy) not in q:
                        q.append((dx, dy))
    return board[n-1][m-1] % 1000000007