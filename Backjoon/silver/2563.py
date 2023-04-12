import sys
input = sys.stdin.readline


confetti_width = 10


def main():
    n = int(input())
    board = list([0] * 100 for _ in range(100))
    res = 0
    for _ in range(n):
        x_1, y_1 = map(int, input().split())
        x_2, y_2 = x_1 + confetti_width, y_1 + confetti_width
        for x in range(x_1-1, x_2-1):
            for y in range(y_1-1, y_2-1):
                if board[x][y] == 0:
                    board[x][y] = 1
                    res += 1
    print(res)




main()