from collections import deque


def BFS(maps, x, y, visited):
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((x, y))
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distance = {(x, y): 0}
    while q:
        x, y = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] is False and maps[dx][dy] == 1:
                if dx == n-1 and dy == m-1:
                    return distance[(x, y)] + 2
                q.append((dx, dy))
                distance[(dx, dy)] = distance[(x, y)] + 1
                visited[dx][dy] = True
    return -1


def solution(maps):
    visited = list([False] * len(maps[0]) for _ in range(len(maps)))
    answer = BFS(maps, 0, 0, visited)
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))