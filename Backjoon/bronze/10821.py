import sys
input = sys.stdin.readline


def main():
    s = list(map(str, input().strip().split(',')))
    res = 0
    for e in s:
        if e.isdigit():
            res += 1
    print(res)


main()
