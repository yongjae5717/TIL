import sys
from collections import deque

# N: 보드의 크기
N = int(sys.stdin.readline())
board = [[0] * N for _ in range(N)]
# K: 사과의 개수
K = int(sys.stdin.readline())

# 사과의 위치
for _ in range(K):
    column, row = map(int, sys.stdin.readline().split())
    board[column-1][row-1] = 1

# L: 뱀의 방향 변환 정보(정수 X와 문자 C)
# X: 몇초 뒤 방향 전환
# C: 'L' -> 왼쪽, 'D' -> 오른쪽

dir_data = dict()
L = int(sys.stdin.readline())
for _ in range(L):
    temp, C = sys.stdin.readline().split()
    X = int(temp)
    dir_data[X+1] = C

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
idx = 0

q = deque([(0, 0)])
time = 0

while True:
    time += 1

    if time in dir_data.keys():
        C = dir_data[time]
        if C == "D":
            idx += 1
        elif C == "L":
            idx -= 1

    x, y = q[0]  # 뱀의 머리
    dx, dy = x + dir[idx % 4][0], y + dir[idx % 4][1]

    if 0 <= dx < N and 0 <= dy < N:
        if board[dy][dx] == 1:
            q.appendleft((dx, dy))
            board[dy][dx] = 0

        elif (dx, dy) in q:
            print(time)
            break

        else:
            q.appendleft((dx, dy))
            q.pop()

    else:
        print(time)
        break