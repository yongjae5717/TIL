from collections import deque


def BFS(n, computers, computer, visited):
    visited[computer] = True
    q = deque()
    q.append(computer)
    while q:
        computer = q.popleft()
        visited[computer] = True
        for i in range(n):
            if i != computer and computers[computer][i] == 1:
                if not visited[i]:
                    q.append(i)


def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            BFS(n, computers, i, visited)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))