import sys
input = sys.stdin.readline


def main():
    s = list(input().strip().split(','))
    res = list()
    for e in s:
        if e.isdigit():
            res.append(int(e))
    print(sum(res))


main()