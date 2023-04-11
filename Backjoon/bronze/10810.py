import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    array = [0] * (n+1)
    for _ in range(m):
        i, j, k = map(int, input().split())
        for d in range(i, j + 1):
            array[d] = k

    print(*array[1:])


main()