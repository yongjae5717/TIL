import sys
input = sys.stdin.readline


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    print(*sorted(arr))


main()