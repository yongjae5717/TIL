import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, r, visited):
    q = deque([r])
    visited[r] = 1
    count = 2

    while q:
        r = q.popleft()

        for i in graph[r]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = count
                count += 1


def main():
    n, m, r = map(int, input().split())

    # visited 리스트
    visited = [0] * (n+1)

    # 간선 정보 (graph)
    graph = list(list() for _ in range(n + 1))
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, n+1):
        graph[i].sort()
    # print(graph)

    bfs(graph, r, visited)

    for i in visited[1:]:
        print(i)


main()