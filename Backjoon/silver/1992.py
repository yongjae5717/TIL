import sys
input = sys.stdin.readline


def main():
    n = int(input())
    board = list(list(map(int, input().strip())) for _ in range(n))
    quad(board, 0, 0, n)


def quad(lst, x, y, n):
    tmp = lst[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if tmp != lst[i][j]:
                tmp = -1
                break

    if tmp == -1:
        print("(", end='')
        n //= 2
        quad(lst, x, y, n)
        quad(lst, x, y+n, n)
        quad(lst, x+n, y, n)
        quad(lst, x+n, y+n, n)
        print(")", end='')
    elif tmp == 1:
        print(1, end='')
    elif tmp == 0:
        print(0, end='')


main()