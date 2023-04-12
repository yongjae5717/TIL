import sys, math
input = sys.stdin.readline


def main():
    a, b = map(int, input().split())

    c, d = map(int, input().split())

    e, f = a * d + b * c, b * d
    gcd = math.gcd(e, f)

    if gcd != 1:
        e //= gcd
        f //= gcd

    print(e, f)


main()