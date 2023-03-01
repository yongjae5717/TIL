import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    keywords = set()
    for _ in range(n):
        keywords.add(input().strip())

    for _ in range(m):
        lst = set(list(input().strip().split(',')))
        keywords -= lst
        print(len(keywords))


main()