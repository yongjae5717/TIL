import sys


def main():
    # 세로길이 N, 가로길이 M
    N, M = map(int, sys.stdin.readline().split())
    result = 1
    height, width = N, M

    if height == 1:
        result = 1
    elif height == 2 and width % 2 == 0:
        result = width // 2
    elif height == 2 and width % 2 == 1:
        result = width // 2 + 1
    elif height >= 3 and width > 6:
        result = width - 2
    elif height >= 3 and width <= 6:
        result = width

    if (width < 7 or height < 3) and result > 4:
        result = 4

    print(result)


main()