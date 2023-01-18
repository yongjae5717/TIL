import sys
input = sys.stdin.readline


def main():
    row, column = map(int, input().split())
    n = int(input())
    points = list(list(map(int, input().split())) for _ in range(n))
    r, c = [0, row], [0, column]
    for t, p in points:
        if t == 0:
            c.append(p)
        elif t == 1:
            r.append(p)
    r.sort()
    c.sort()

    max_r, max_c = 0, 0
    for i in range(1, len(r)):
        max_r = max(max_r, r[i] - r[i-1])
    for i in range(1, len(c)):
        max_c = max(max_c, c[i] - c[i-1])

    print(max_c * max_r)


main()