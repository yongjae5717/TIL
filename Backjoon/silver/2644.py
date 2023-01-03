import sys
from collections import deque
input = sys.stdin.readline


def main():
    n = int(input())
    start, end = map(int, input().split())
    m = int(input())
    graph = list([] for _ in range(n + 1))
    visited = list(-1 for _ in range(n + 1))

    for i in range(m):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    relations = deque()
    visited[start] = 0
    relations.append(start)
    while relations:
        x = relations.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                relations.append(i)
    print(visited[end])


main()