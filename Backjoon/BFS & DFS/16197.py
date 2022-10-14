"""
N x M 크기의 보드와 4개의 버튼으로 이루어진 게임
버튼은 상하좌우 4가지가 있다.
버튼을 누르면 두 동전이 버튼에 쓰여있는 방향으로 동시에 이동한다.
1. 벽이면 동전은 이동하지 않는다
2. 이동하려는 칸에 칸이 없으면 동전은 떨어진다
3. 그 외의 경우에는 원하는 방향으로 이동한다.
두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇번 눌러야 할까?

o: 동전
.: 빈 칸
#: 벽

동전의 개수는 항상 2개
"""

import sys
from collections import deque


def BFS(board, coins_location):
    d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    coin = deque()
    coin.append(coins_location)
    while coin:
        x1, y1, x2, y2, count = coin.popleft()
        # 10번보다 더 많은 버튼을 눌러야한다면 -1출력
        if count >= 10:
            return -1
        for i in range(len(d)):
            dx1 = x1 + d[i][0]
            dy1 = y1 + d[i][1]
            dx2 = x2 + d[i][0]
            dy2 = y2 + d[i][1]
            # 두개 코인이 전부 안떨어졌을 때
            if (0 <= dx1 < N) and (0 <= dy1 < M) and (0 <= dx2 < N) and (0 <= dy2 < M):
                if board[dx1][dy1] == "#":
                    dx1, dy1 = x1, y1
                if board[dx2][dy2] == "#":
                    dx2, dy2 = x2, y2
                coin.append((dx1, dy1, dx2, dy2, count + 1))
            # coin 2가 떨어지는 경우
            elif (0 <= dx1 < N) and (0 <= dy1 < M):
                return count + 1
            # coin 1가 떨어지는 경우
            elif (0 <= dx2 < N) and (0 <= dy2 < M):
                return count + 1
    return -1


N, M = map(int, sys.stdin.readline().split())
board = list([""] * M for _ in range(N))
coins_location = list()
for i in range(N):
    input_string = sys.stdin.readline().strip()
    for j in range(M):
        board[i][j] = input_string[j]
        if board[i][j] == 'o':
            coins_location.append(i)
            coins_location.append(j)
coins_location.append(0)  # count까지 deque에 추가하기 위함

print(BFS(board, coins_location))