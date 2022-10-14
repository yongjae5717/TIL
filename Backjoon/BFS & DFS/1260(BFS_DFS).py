import sys
from collections import deque

# DFS: 모든 노드를 방문하고 싶을 때 사용한다.
# DFS: Root node 시작으로 다음 분기까지 넘어가기 전에 완전히 탐색하는 것
# 한 방항으로 계속 탐색을 하다가 더 이상 탐색할 수 없을 때, 갈림길로 돌아와 완전 탐색
# DFS: 어떤 노드를 방문했었는지 여부를 반드시 확인해야한다.

# BFS: Root node 시작해서 인접한 노드를 먼저 탐색하는 방법
# 시작 점에서 가까운 점 먼저 방문 --> 최단 경로나 임의의 경로를 찾고 싶을 때 사용
# 재귀적으로 동작하지 않으며, 큐를 이용하여 반복적 형태로 구현

N, M, V = map(int, sys.stdin.readline().split())
# 0번 인덱스는 무시하기 위해서 N이 아닌 N+1 이용
checked = [0] * (N + 1)
checked2 = [0] * (N + 1)
graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1
# print(graph)
# for i in graph:
#     print(i)


def dfs(V):
    # print(checked)
    checked[V] = 1
    print(V, end=" ")

    for i in range(1, N+1):
        if checked[i] == 0 and graph[V][i] == 1:
            dfs(i)


def bfs(V):
    q = deque()
    q.append(V)
    checked2[V] = 1

    while q:
        V = q.popleft()
        print(V, end=" ")

        for i in range(1, N+1):
            if checked2[i] == 0 and graph[V][i] == 1:
                q.append(i)
                checked2[i] = 1


dfs(V)
print("")
bfs(V)