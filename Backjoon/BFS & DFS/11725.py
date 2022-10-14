import sys
from collections import deque

N = int(sys.stdin.readline())
tree = list([] for _ in range(N+1))
for i in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)
# print(tree)


def BFS(start):
    q = deque()
    q.append(start)
    visited = [0] * (N+1)
    visited[start] = 1
    while q:
        temp = int(q.popleft())
        for node in tree[temp]:
            if visited[node] == 0:
                visited[node] = 1
                result.append((node, temp))
                q.append(node)


result = list()
BFS(1)
# print(result)
result.sort()
for ans in result:
    print(ans[1])