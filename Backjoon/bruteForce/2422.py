import sys
from itertools import combinations
input = sys.stdin.readline


n, m = map(int, input().split())

board = list([0] * n for _ in range(n))

result = 0

for i in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
    board[b-1][a-1] = 1

for c in combinations(range(n), 3):
    x, y, z = c
    if board[x][y] != 1 and board[x][z] != 1 and board[y][z] != 1:
        result += 1

print(result)