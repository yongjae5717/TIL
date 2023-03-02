import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    q, r = divmod(n, 2)
    print(lst[q + r - 1])


main()