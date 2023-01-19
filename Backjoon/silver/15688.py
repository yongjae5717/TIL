import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lst = list(int(input()) for _ in range(n))
    lst.sort()

    for p in lst:
        print(p)


main()