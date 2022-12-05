import sys
input = sys.stdin.readline

h, w = map(int, input().split())
lst = list(map(int, input().split()))


def solution(n, m, temp):
    board = list([0] * m for _ in range(n))
    index_board = list(list() for _ in range(n))
    for i in range(m):
        height = temp[i]
        for j in range(height):
            board[j][i] = 1
            index_board[j].append(i)

    result = 0
    for i in index_board:
        if len(i) >= 2:
            result += (i[-1]-i[0]) + 1 - len(i)
    return result


print(solution(h, w, lst))