import sys


def board_max_value(board, N):
    row_count, col_count = 1, 1
    # 행 개수 확인
    for i in range(N):
        temp = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]:
                temp += 1
            else:
                row_count = max(row_count, temp)
                temp = 1
        row_count = max(row_count, temp)

    # 열 개수 확인
    for i in range(N):
        temp = 1
        for j in range(1, N):
            if board[j-1][i] == board[j][i]:
                temp += 1
            else:
                col_count = max(col_count, temp)
                temp = 1
        col_count = max(col_count, temp)

    return max(row_count, col_count)


# 0. N x N 행렬에 사탕을 채워넣는다.
N = int(sys.stdin.readline())
board = list([""] * N for _ in range(N))
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

for i in range(N):
    line = sys.stdin.readline().strip()
    for j in range(N):
        board[i][j] = line[j]

max_count = board_max_value(board, N)

# 1. 사탕의 색이 다른 인접한 두칸을 고른다.
for i in range(N):
    for j in range(N):
        for k in range(len(d)):
            dx = i + d[k][0]
            dy = j + d[k][1]
            # 2. 인접한 두칸을 교환하고 개수확인 후 다시 교환
            if 0 <= dx < N and 0 <= dy < N:
                if board[i][j] != board[dx][dy]:
                    board[i][j], board[dx][dy] = board[dx][dy], board[i][j]
                    max_count = max(max_count, board_max_value(board, N))
                    board[i][j], board[dx][dy] = board[dx][dy], board[i][j]

print(max_count)