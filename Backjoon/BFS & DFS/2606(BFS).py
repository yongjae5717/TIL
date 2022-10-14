import sys
from collections import deque

N = int(sys.stdin.readline())
link_N = int(sys.stdin.readline())
array = list([0] * (N + 1) for _ in range(N + 1))

for _ in range(link_N):
    x, y = map(int, sys.stdin.readline().split())
    array[x][y] = 1
    array[y][x] = 1


def BFS():
    q = deque()
    q.append(1)
    visited = list()
    while q:
        temp = q.popleft()
        visited.append(temp)

        for i in range(len(array)):
            if array[temp][i] and i not in visited and i not in q:
                q.append(i)
    return len(visited)


print(BFS() - 1)