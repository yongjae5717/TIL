import sys
input = sys.stdin.readline
from collections import deque


def BFS(matrix, visit, l):
    q = deque()
    q.append((0, 0))
    # 오른쪽 or 아래
    d = [(1, 0), (0, 1)]
    while q:
        x, y = q.popleft()
        val = matrix[x][y]

        # 종료지점에 도착했을 떄
        if matrix[x][y] == -1:
            return "HaruHaru"

        for i in range(len(d)):
            dx = x + d[i][0] * val
            dy = y + d[i][1] * val
            if (0 <= dx < l) and (0 <= dy < l):
                # 방문 했더라면 다음 인덱스로 넘어간다.(이로인해서 메모리를 덜 사용)
                if visit[dx][dy]:
                    continue
                # 방문하지 않았다면 방문으로 변경한다.
                else:
                    visit[dx][dy] = True
                    q.append((dx, dy))
    return "Hing"


# make board matrix (N x N) & visited matrix
n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))
visited = list([False] * n for _ in range(n))
print(BFS(board, visited, n))