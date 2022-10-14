import sys
from collections import deque


def BFS():
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((0, 0))
    result = 0
    while q:
        x, y = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if (0 <= dx < W) and (0 <= dy < H) and array[dx][dy] != 0:
                if array[dx][dy] == '0':
                    array[dx][dy] = 0
                    q.append((dx, dy))
                if array[dx][dy] == '1':
                    array[dx][dy] = 0
                    result += 1
    return result


W, H = map(int, sys.stdin.readline().split())
array = list()
for i in range(W):
    temp = list(map(str, sys.stdin.readline().split()))
    array.append(temp)
# print(array)

time = 0
result_array = list()

while True:
    cheese = BFS()
    result_array.append(cheese)
    time += 1

    if cheese == 0:
        time -= 1
        break
    for i in range(W):
        array[i] = list(map(str, array[i]))

print(time)
print(result_array[time - 1])