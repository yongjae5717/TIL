from collections import deque


def solution(n, edge):
    distance = [0] * (n+1)
    distance[1] = 1
    graph = [[] for _ in range(n+1)]
    q = deque([1])

    # 노드 구성
    for i in sorted(edge):
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    # 간선 간 거리 계산
    while q:
        x = q.popleft()
        for node in graph[x]:
            if distance[node] == 0:
                q.append(node)
                distance[node] = distance[x] + 1
    max_value = max(distance)
    return distance.count(max_value)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))