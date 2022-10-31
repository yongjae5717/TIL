from collections import deque


def BFS(begin, target, words, visited):
    q = deque()
    q.append((begin, 0))
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append((words[i], cnt+1))
                    visited[i] = True


def solution(begin, target, words):
    visited = [False for _ in range(len(words))]
    if target not in words:
        return 0
    return BFS(begin, target, words, visited)


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))