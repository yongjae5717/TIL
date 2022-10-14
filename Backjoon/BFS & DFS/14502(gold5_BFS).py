import copy
import sys
from collections import deque


def BFS(array_x, s, e):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((s, e))
    polluted_zone = 0
    while q:
        x, y = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if (0 <= dx < N) and (0 <= dy < M) and array_x[dx][dy] == 0:
                array_x[dx][dy] = 2
                q.append((dx, dy))
                polluted_zone += 1
    return polluted_zone


N, M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
safe_list = list()
virus_list = list()
safe_zone = 0

for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            safe_list.append((i, j))
            safe_zone += 1
        elif array[i][j] == 2:
            virus_list.append((i, j))

safe_number = len(safe_list)

result_list = list()
for i in range(safe_number):
    for j in range(i + 1, safe_number):
        for k in range(j + 1, safe_number):
            total_pol = 0
            # deepcopy
            graph = copy.deepcopy(array)
            x1, y1 = safe_list[i]
            x2, y2 = safe_list[j]
            x3, y3 = safe_list[k]
            graph[x1][y1] = 1
            graph[x2][y2] = 1
            graph[x3][y3] = 1
            for s in virus_list:
                x, y = s
                total_pol += BFS(graph, x, y)
            result_list.append(safe_number - 3 - total_pol)

print(max(result_list))