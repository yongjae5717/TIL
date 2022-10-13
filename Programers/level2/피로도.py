answer = 0
visited = list()


def dfs(k, dungeons):
    global answer
    answer = max(answer, sum(visited))

    for i in range(len(dungeons)):
        condition, needFatigue = dungeons[i]
        if not visited[i] and k >= condition:
            visited[i] = 1
            dfs(k-needFatigue, dungeons)
            visited[i] = 0


def solution(k, dungeons):
    global answer, visited
    visited = [0] * len(dungeons)
    dfs (k, dungeons)
    return answer