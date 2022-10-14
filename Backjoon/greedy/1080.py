import sys


def flip(line, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            line[i][j] = 1 - line[i][j]


def main():
    N, M = map(int, sys.stdin.readline().split())
    lines_A = list()
    lines_B = list()
    result = 0

    for _ in range(N):
        lines_A.append(list(map(int, sys.stdin.readline().rstrip())))

    for _ in range(N):
        lines_B.append(list(map(int, sys.stdin.readline().rstrip())))

    for i in range(N - 2):
        for j in range(M - 2):
            if lines_A[i][j] != lines_B[i][j]:
                flip(lines_A, i, j)
                result += 1

    if lines_A != lines_B:
        print("-1")
    else:
        print(result)


main()