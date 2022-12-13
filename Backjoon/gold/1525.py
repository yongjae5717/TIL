import sys

input = sys.stdin.readline
from collections import deque

chart, board = "", dict()
for _ in range(3):
    chart += "".join(input().split())


def bfs(chart):
    q = deque()
    q.append(chart)
    board[chart] = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        now = q.popleft()
        if now == "123456780":
            return board[now]
        location = now.find("0")
        x, y = location % 3, location // 3

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            n_location = ny * 3 + nx
            if 0 <= nx < 3 and 0 <= ny < 3:
                now_list = list(now)
                now_list[location], now_list[n_location] = now_list[n_location], now_list[location]
                nxt = ''.join(now_list)
                if nxt not in board.keys():
                    board[nxt] = board[now] + 1
                    q.append(nxt)
    return -1


print(bfs(chart))
