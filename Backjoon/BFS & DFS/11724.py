import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

array = list([0] * (N+1) for _ in range(N+1))

# make graph
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    array[x][y] = 1
    array[y][x] = 1

# for k in array:
#     print(k)

# BFS
visited = [0] * (N + 1)


def BFS(V):
    q = deque()
    q.append(V)
    visited[V] = 1
    while q:
        V = q.popleft()
        for i in range(1, N + 1):
            if visited[i] == 0 and array[V][i] == 1:
                q.append(i)
                visited[i] = 1


result = 0
for j in range(1, N + 1):
    if visited[j] == 0:
        BFS(j)
        result += 1

print(result)