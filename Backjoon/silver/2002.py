import sys
input = sys.stdin.readline


def main():
    n = int(input())
    dg = dict()
    for i in range(n):
        dg[input().strip()] = i

    ys = list(input().strip() for _ in range(n))

    res = 0
    for i in range(n):
        for j in range(i, n):
            if dg[ys[i]] > dg[ys[j]]:
                res += 1
                break
    print(res)


main()