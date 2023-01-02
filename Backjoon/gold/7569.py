import sys
from collections import deque
input = sys.stdin.readline


def main():
    m, n, h = map(int, input().split())
    box = list()
    q = deque([])

    # box 생성 및 queue에 익은 토마토 저장
    for z in range(h):
        board = list()
        for x in range(n):
            board.append(list(map(int, input().split())))
            for y in range(m):
                if board[x][y] == 1:
                    q.append([z, x, y])
        box.append(board)

    # 너비 우선 탐색
    d = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while q:
        z, x, y = q.popleft()
        for i in d:
            nz, nx, ny = z + i[0], x + i[1], y + i[2]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0:
                    q.append([nz, nx, ny])
                    box[nz][nx][ny] = box[z][x][y] + 1

    # 총 날짜 계산
    day = 0
    for b in box:
        for line in b:
            if line.count(0) != 0:
                print(-1)
                exit()
            day = max(day, max(line))
    print(day-1)


main()