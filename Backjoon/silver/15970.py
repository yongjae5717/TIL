import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lst = list([] for _ in range(n + 1))
    points = list(list(map(int, input().split())) for _ in range(n))
    for point in points:
        loc, color = point
        lst[color].append(loc)

    res = 0
    for l in lst:
        l.sort()
        tmp = 0
        for i in range(len(l)):
            if i == 0:
                tmp += l[i+1] - l[i]
            elif i == len(l)-1:
                tmp += l[i] - l[i-1]
            else:
                tmp += min(l[i+1] - l[i], l[i] - l[i-1])

        res += tmp
    print(res)


main()
