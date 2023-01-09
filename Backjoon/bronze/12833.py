import sys
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    for _ in range(c % 2):
        a ^= b
    return a


print(main())