import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    s = set(input().strip() for _ in range(n))
    check = list(input().strip() for _ in range(m))

    result = 0
    for w in check:
        if w in s:
            result += 1
    return result


print(main())