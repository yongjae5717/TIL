import sys
input = sys.stdin.readline


def main():
    n = int(input())
    print(2**n - 1)
    hanoi(n, 1, 3)


def hanoi(n, loc, des):
    tmp = 6 - loc - des
    if n == 0:
        return
    hanoi(n-1, loc, tmp)
    print(loc, des)
    hanoi(n-1, tmp, des)


main()