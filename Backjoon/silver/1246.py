import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    p = sorted(list(int(input()) for _ in range(m)))
    price = 0
    max_result = -1
    for i in range(m):
        if m - i <= n:
            result = (m - i) * p[i]
        else:
            result = n * p[i]

        if result > max_result:
            price = p[i]
            max_result = result

    print(price, max_result)


main()