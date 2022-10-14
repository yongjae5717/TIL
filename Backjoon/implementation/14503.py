import sys

N, M = map(int, sys.stdin.readline().split())
x, y, front = map(int, sys.stdin.readline().split())

maps = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

result = 1
flag = 0

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    for i in range(len(d)):
        front = (front-1) % 4
        dx = x + d[front][0]
        dy = y + d[front][1]

        if maps[dx][dy] == 0:
            x, y = dx, dy
            maps[x][y] = 2
            result += 1
            break

        if i == 3:
            dx = x - d[front][0]
            dy = y - d[front][1]
            if maps[dx][dy] == 1:
                flag = 1
            else:
                x, y = dx, dy

    if flag:
        break

print(result)