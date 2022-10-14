"""
itertool 모듈을 사용할 수 없을 경우에 조합을 구할 수 있는 문제
"""
import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(i for i in range(1, N+1))
result = list()


def DFS():
    global result, lst, N, M
    if len(result) == M:
        print(*result)
        return

    for i in range(0, N):
        if lst[i] not in result:
            result.append(lst[i])
            DFS()
            result.pop()


DFS()