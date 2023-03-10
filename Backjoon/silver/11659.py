import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    s = [0]
    tmp = 0
    for i in num:
        tmp += i
        s.append(tmp)

    for _ in range(m):
        i, j = map(int, input().split())
        res = s[j] - s[i-1]
        print(res)


main()