import sys
from collections import deque


# use BFS
def BFS(array_x, s, e, val):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((s, e))
    while q:
        x, y = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < N and 0 <= dy < M and array_x[dx][dy] == val:
                array_x[dx][dy] = 0
                q.append((dx, dy))


T = int(sys.stdin.readline())
result = list()
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    array = list([0] * M for _ in range(N))
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        array[y][x] = 1

    cnt_1 = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] != 0:
                cnt_1 += 1
                BFS(array, i, j, array[i][j])
    # print("\n")
    # for j in array:
    #     print(j)
    result.append(cnt_1)

for k in result:
    print(k)