import sys, math
input = sys.stdin.readline


def main():
    n = int(input())
    radius = list(map(int, input().split()))
    standard = radius[0]
    for i in range(1, n):
        tmp = math.gcd(radius[i], standard)
        res = ""
        res += str(standard // tmp) + "/" + str(radius[i] // tmp)
        print(res)


main()